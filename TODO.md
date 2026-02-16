# Passman TODO
**Author**: Muneeb Mennad\
**Project Name**: Passman\
**File Name**: TODO.md\
**Project Start**: 2026-01-24\
**Github Profile**: https://github.com/mnbmnd/
___
## Current
- [ ] Fix logging in logic
- [ ] Fix quitting logic
- [ ] Work on implementing this with vim keys or other keybinds

## Hand-off
- [ ] Update README.md

## Later
- [ ] Add Settings menu for updating master password
  - Require login first
  - Verify old password before allowing update
  
- [ ] Implement password vault storage (`passwords.json`)
  - Encrypt vault with key derived from master password
  - Add check for vault file to prevent credential overwrites

- [ ] Add fuzzy matching for `passman <site>` CLI
  - Install `rapidfuzz`
  - Implement site name matching

- [ ] Add clipboard support
  - Install `pyperclip`
  - Auto-copy passwords on retrieval

- [ ] Add TUI (when going full scale)
  - Consider `prompt_toolkit` or `textual`
  - Add Enter/ESC navigation

## Completed ✓
- [x] Master password authentication with PBKDF2
- [x] Password generation (passphrase + alphanumeric)
- [x] Entropy/strength checker
- [x] Menu system
- [x] Add `has_master_credentials()` function to `authentication.py`
- [x] Update `credentials_menu()` in `main.py`
- [x] Test both scenarios
- [x] Fix functions and file structure

###### END_FILE  
