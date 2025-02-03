[Setup]
AppName=FocusTimer
AppVersion=1.0
DefaultDirName={pf}\FocusTimer
DefaultGroupName=FocusTimer
OutputBaseFilename=FocusTimerInstaller
Compression=lzma
SolidCompression=yes

[Files]
Source: "dist\FocusTimer\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\FocusTimer"; Filename: "{app}\FocusTimer.exe"
Name: "{commondesktop}\FocusTimer"; Filename: "{app}\FocusTimer.exe"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Create Desktop Icon"; GroupDescription: "Additional icons:"