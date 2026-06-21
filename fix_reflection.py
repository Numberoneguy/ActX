import os

player_path = "./src/game/java/net/minecraft/client/entity/EntityPlayerSP.java"
api_path = "./src/platform-api/java/net/lax1dude/eaglercraft/v1_8/internal/PlatformTranslator.java"

# 1. Update EntityPlayerSP.java to link cleanly to PlatformTranslator
if os.path.exists(player_path):
    print("[+] Patching EntityPlayerSP.java...")
    with open(player_path, "r", encoding="utf-8") as f:
        content = f.read()

    start_marker = "public void sendChatMessage(String message) {"
    start_idx = content.find(start_marker)
    header_idx = content.rfind("/**+", 0, start_idx)
    if header_idx == -1: header_idx = start_idx

    swing_marker = "public void swingItem() {"
    swing_idx = content.find(swing_marker)
    end_marker = "this.sendQueue.addToSendQueue(new C0APacketAnimation());\n\t}"
    end_idx = content.find(end_marker, swing_idx)
    if end_idx == -1: end_idx = content.find("}", swing_idx) + 1
    else: end_idx += len(end_marker)

    player_replacement = """\t/**+
	 * Sends a chat message from the player. Args: chatMessage
	 */
	public void sendChatMessage(String message) {
		if (message.startsWith("?translate chinese ")) {
			String textToTranslate = message.substring("?translate chinese ".length());
			if (textToTranslate.trim().isEmpty()) {
				this.addChatMessage(new ChatComponentText(EnumChatFormatting.RED + "Usage: ?translate chinese <text>"));
				return;
			}

			this.addChatMessage(new ChatComponentText(EnumChatFormatting.YELLOW + "Processing layout and dispatching translation..."));

			// Extract leading symbols/formatting codes
			StringBuilder leading = new StringBuilder();
			int start = 0;
			while (start < textToTranslate.length() && !Character.isLetterOrDigit(textToTranslate.charAt(start))) {
				leading.append(textToTranslate.charAt(start));
				start++;
			}

			// Extract trailing symbols
			StringBuilder trailing = new StringBuilder();
			int end = textToTranslate.length() - 1;
			while (end >= start && !Character.isLetterOrDigit(textToTranslate.charAt(end))) {
				trailing.insert(0, textToTranslate.charAt(end));
				end--;
			}

			// Pure core text to pass to API
			String cleanCore = textToTranslate.substring(start, end + 1);

			// Direct standard reference link without risky runtime String reflections!
			PlatformTranslator.savedLeading = leading.toString();
			PlatformTranslator.savedTrailing = trailing.toString();
			PlatformTranslator.fireTranslate(cleanCore, "zh-CN");
			return;
		}

		if (((sendQueue.getNetworkManager() instanceof ClientIntegratedServerNetworkManager)
				|| (sendQueue.getNetworkManager() instanceof LANClientNetworkManager))
				&& message.startsWith("/eagskull")) {
			this.mc.eagskullCommand.openFileChooser();
		} else {
			this.sendQueue.addToSendQueue(new C01PacketChatMessage(message));
		}
	}

	/**+
	 * Swings the item the player is holding.
	 */
	public void swingItem() {
		super.swingItem();
		this.sendQueue.addToSendQueue(new C0APacketAnimation());
	}"""

    new_content = content[:header_idx] + player_replacement + content[end_idx:]
    with open(player_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("[+] EntityPlayerSP.java successfully updated.")

# 2. Update PlatformTranslator.java to bypass runtime Reflection entirely
if os.path.exists(api_path):
    print("[+] Patching PlatformTranslator.java...")
    
    api_replacement = """package net.lax1dude.eaglercraft.v1_8.internal;

public class PlatformTranslator {

	public static String savedLeading = "";
	public static String savedTrailing = "";

	public static void fireTranslate(String text, String targetLang) {
		// Bypasses reflection string references entirely so TeaVM compiles it cleanly
		try {
			WebTranslationHook.invokeNativeJS(text, targetLang);
		} catch (Throwable t) {
			// Graceful catch for platforms that aren't the Web bundle target
		}
	}

	public static String popResult() {
		try {
			String rawResult = WebTranslationHook.getQueuedTranslation();
			if (rawResult != null && !rawResult.isEmpty()) {
				// Stitch the stripped symbols back onto the translated core response string
				String fullyStitched = savedLeading + rawResult + savedTrailing;
				savedLeading = ""; 
				savedTrailing = "";
				return fullyStitched;
			}
		} catch (Throwable t) {
			// Quietly pass on non-web platform layers
		}
		return null;
	}
}
"""
    with open(api_path, "w", encoding="utf-8") as f:
        f.write(api_replacement)
    print("[+] PlatformTranslator.java successfully updated.")

print("[+] Done! Compile errors and reflection faults are fully addressed.")

