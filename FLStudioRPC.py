import time
from pypresence import Presence
import pygetwindow as gw
import psutil

client_id = '1267256841063239691'
RPC = Presence(client_id)
RPC.connect()
start_time = None
current_project_name = None

# Get current time in Unix
def get_current_unix_time():
    return int(time.time())

# Find FL Studio's process
def is_fl_studio_process_present():
  for proc in psutil.process_iter(['name']):
    if proc.info['name'] == 'FL64.exe':
      return True
  return False
      
# Find FL Studio's window
def find_fl_studio_window():
    windows = gw.getWindowsWithTitle('FL Studio')
    for window in windows:
        if ' - FL Studio' in window.title:
            return window.title
        elif 'FL Studio' in window.title:
            return "Blank"
    return None

# Get the project's name from the window
def get_current_project(title):
    if title and title != "Blank":
        project_name = title.split(' - ')[0]
        return project_name
    return "A Project"

# Update Rich Presence
def update_rpc():
    global current_project_name, start_time
    
    window_title = find_fl_studio_window()
    project_name = get_current_project(window_title)
    
    if window_title:
      if project_name != current_project_name: # Check if its a new project
          current_project_name = project_name  # Update current new project
          start_time = get_current_unix_time() # Get new timestamp
      # Update Rich Presence
      RPC.update(
          large_text="FL Studio",
          state=f"Working on {project_name}",
          large_image="fl-studio-logo",
          start=start_time
      )
    else:
        RPC.clear()   # Clear presence
        return False  # Indicates that FL Studio is not Running
    return True       # Indicates that FL Studio is running
    
if __name__ == "__main__":
  while True:
    if is_fl_studio_process_present():
      if not update_rpc():
        # If FL Studio is not running
        break     
    else:
      RPC.clear()
      break # Exit if FL Studio process is not found
    time.sleep(5)
