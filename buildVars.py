# -*- coding: UTF-8 -*-
from site_scons.site_tools.NVDATool.typings import AddonInfo, BrailleTables, SymbolDictionaries
from site_scons.site_tools.NVDATool.utils import _

addon_info = AddonInfo(
    addon_name="VisionAssistant",
    # Add-on summary/title, usually the user visible name of the add-on
    # Translators: Summary/title for this add-on
    # to be shown on installation and add-on information found in add-on store
    addon_summary=_("Vision Assistant Pro"),
# Add-on description
    # Translators: Long description to be shown for this add-on on add-on information from add-on store
    addon_description=_("""An advanced AI assistant for NVDA using Gemini models.
Command Layer: Press NVDA+Shift+V, then:
- Smart Translator (T) / Clipboard (Shift+T)
- Text Refiner (R)
- Describe Object (V) / Full Screen (O)
- Online Video Analysis (Shift+V)
- Document Reader (D)
- File OCR (F)
- CAPTCHA Solver (C)
- Audio Transcription (A)
- Smart Dictation (S)
- Announce Status (I)
- Label Object (L)
- Manage/Scan Labels (Shift+L)
- UI Explorer (E)
- AI Operator (Shift+A)
- Check Update (U)
- Recall Last Result (Space)
- Commands Help (H)"""),
    addon_version="7.0",
    # Brief changelog for this version
    # Translators: what's new content for the add-on version to be shown in the add-on store
    addon_changelog=_("""## Changes for 7.0.0

*   **Resuming Unfinished Scans**: Added a resume feature for both the Document Reader and Smart File Actions. If a scan gets interrupted, you can now continue from where it stopped instead of starting over from scratch.
*   **New `[screen_fg_obj]` Variable**: Added a custom prompt variable to capture a screenshot of only the active foreground window rather than the entire screen.
*   **Smart Retries & Key Rotation**: The addon now silently retries up to 5 times on the same key when hitting temporary server overloads (like "high demand" or malformed responses). If the retries fail, it automatically switches to the next API key in your list.
*   **Screen Curtain Detection**: Added a check to prevent taking screenshots when the Screen Curtain is active (whether permanently enabled or toggled temporarily with the hotkey). It will warn you and stop, preventing you from sending black images and wasting API tokens.
*   **Document Reader Tweaks**: The PDF range dialog now automatically pre-selects the default target language from your addon settings. Also improved thread handling to make sure background tasks stop cleanly when the reader is closed.
*   **Native Mistral OCR Integration**: Integrated Mistral's native Document OCR API. Multi-page documents are automatically merged, uploaded, and processed in batches using Mistral's specialized `/v1/ocr` endpoint, while single-page images are processed directly without unnecessary PDF conversions [1].
*   **Dynamic Custom URL Handlers**: Modifying the Custom API URL now instantly clears the cached model list and restores the manual model entry text box. This ensures full compatibility with custom endpoints (such as Cloudflare AI Gateway) that do not support the standard `/v1/models` listing endpoint.
*   **Overhauled AI Operator Input Engine**: Completely rewritten the underlying mouse and keyboard simulation system for the AI Operator. Replaced the legacy `mouse_event` API with the modern Windows `SendInput` API, bringing significantly higher compatibility with modern applications, UAC-protected windows, and high-DPI displays.
*   **Fixed Drag & Drop Operations**: Drag and drop actions in the AI Operator are now fully stable and reliable. The new engine uses natural "easing" curves, precise cursor positioning, optimized timing, and a smart "nudge" technique to ensure that Windows and applications correctly recognize and execute drag-and-drop gestures without failing mid-way.
*   **Multi-Monitor Support**: The AI Operator now fully supports multi-monitor setups. Mouse movements and clicks work correctly across all monitors using the `MOUSEEVENTF_VIRTUALDESK` flag, ensuring accurate positioning regardless of which monitor the target application is on.
*   **Enhanced Keyboard Simulation**: Improved keystroke injection to fully support "Extended Keys" (such as Arrow keys, Home, End, Page Up/Down, Insert, Delete, and F1-F12). This ensures that navigation and shortcut commands sent by the AI Operator work flawlessly across all applications.
*   **HEIC/HEIF Image Support**: Added native support for iPhone photo formats. You can now directly select `.heic` and `.heif` files for AI description, OCR, or Document Reading without prior conversion."""),
    addon_author="Mahmood Hozhabri",
    addon_url="https://github.com/mahmoodhozhabri/VisionAssistantPro",
    addon_sourceURL="https://github.com/mahmoodhozhabri/VisionAssistantPro",
    addon_docFileName="readme.html",
    addon_minimumNVDAVersion="2025.1",
    addon_lastTestedNVDAVersion="2026.1",
    addon_updateChannel=None,
    addon_license="GPL-2.0",
    addon_licenseURL="https://www.gnu.org/licenses/gpl-2.0.html",
)

pythonSources: list[str] = ["addon/globalPlugins/visionAssistant/*.py"]
i18nSources = pythonSources + ["buildVars.py"]
excludedFiles: list[str] = []

baseLanguage: str = "en"

markdownExtensions: list[str] = [
    "markdown.extensions.tables",
    "markdown.extensions.toc",
    "markdown.extensions.nl2br",
    "markdown.extensions.extra",
]

brailleTables: BrailleTables = {}
symbolDictionaries: SymbolDictionaries = {}