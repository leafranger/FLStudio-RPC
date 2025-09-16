
<div>
<h1> FL Studio Discord Rich Presence
<img src="assets/icon.ico" alt="FL Studio RPC Icon" width="48"/>
</div>


This project integrates Discord Rich Presence with FL Studio, allowing you to display the project you're working on in your Discord status. When you start FL Studio and the Rich Presence application, it will show your current project in Discord and automatically update as you work.

## Installation

To set up the FL Studio Discord Rich Presence integration, follow these steps:

1. **Download the ZIP File:**
   - Obtain the ZIP file containing the necessary files from the repository.

2. **Extract the ZIP File:**
   - Extract the contents of the ZIP file to a location on your computer.

3. **Move the Extracted Content:**
   - Move the extracted folder to the same directory where `FL64.exe` (the FL Studio executable) is located. This ensures that all components are in the correct directory.

4. **Run the Batch File:**
   - Double-click the `FLStudioRPC.bat` file to start FL Studio and the Rich Presence application. The batch file will open FL Studio and the Rich Presence executable.

5. **Shortcut:**
   - For future use, the batch file will create a shortcut of itself on your desktop. This shortcut allows you to easily start FL Studio and the Rich Presence application with a single click.

## Usage
- **First time**
  - As said above, the first time you have to run the batch file from the same directory as `FL64.exe`
 
- **Starting FL Studio and Rich Presence:**
  - Simply use the desktop shortcut created by the batch file. This will start FL Studio and the Discord Rich Presence application, updating your Discord status with the project you are working on.

- **Updating the Presence:**
  - The Rich Presence application will automatically update your Discord status based on the current project in FL Studio. It will show "Working on" and then the project name in Discord. It will just say "Working on A Project" if it fails to identify the project's name or you're working on an untitled/blank project.

## Additional Notes

- **Troubleshooting:**
  - If FL Studio or the Rich Presence application does not start correctly, ensure that all files are in the correct directory and that `FL64.exe` is present.

- **Dependencies:**
  - This setup assumes that you have FL Studio installed and that the executables and assets are correctly placed in the same directory as `FL64.exe`.

## Changelog
### v1.0.1
- Batch script fix

### v1.0.0
- First public working release
- In future updates there may not be any need for the exe file or batch script, Rich presence will work automatically when opening FL Studio.

## License

This project is licensed under the GNU General Public License v3.0 License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or issues, please open an issue on the [GitHub repository](https://github.com/leafranger/FLStudio-RPC/issues) or contact the repository owner directly.

---

Happy music-making and Discord presence displaying!
