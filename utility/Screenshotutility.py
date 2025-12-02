import os

def capture_screenshot(item, file_path):#capture_screenshot take a screenshot using a Selenium WebDriver that is stored inside a pytest fixture (browserinstance) and save it to a file
    """
    Captures and saves a screenshot using the driver found in 'item'.
    Returns the file path if successful, else None.
    """
    driver = None
    '''Pytest stores fixture values in item.funcargs.
    This checks whether the current test used the fixture named "browserinstance".
    If so, it extracts that fixture—this is expected to be your Selenium WebDriver'''

    if hasattr(item, 'funcargs') and 'browserinstance' in item.funcargs:
        driver = item.funcargs['browserinstance']
    '''
    if driver is found, Ensures the folder exists before saving the screenshot (os.makedirs(..., exist_ok=True) prevents errors if the folder already exists).
    Calls Selenium’s save_screenshot() to write the PNG file.
    Prints a message and returns the file path'''
    if driver:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)  # Ensure directory exists
        driver.save_screenshot(file_path)
        print(f"[Screenshot] Saved to: {file_path}")
        return file_path
    else:
        print("[Screenshot] Driver not found; skipping screenshot.")
        return None