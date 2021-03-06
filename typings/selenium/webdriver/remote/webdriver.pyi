"""
This type stub file was generated by pyright.
"""

from contextlib import contextmanager
from typing import Any, Optional

"""The WebDriver implementation."""
_W3C_CAPABILITY_NAMES = frozenset(['acceptInsecureCerts', 'browserName', 'browserVersion', 'platformName', 'pageLoadStrategy', 'proxy', 'setWindowRect', 'timeouts', 'unhandledPromptBehavior'])
_OSS_W3C_CONVERSION = { 'acceptSslCerts': 'acceptInsecureCerts','version': 'browserVersion','platform': 'platformName' }
def _make_w3c_caps(caps):
    """Makes a W3C alwaysMatch capabilities object.

    Filters out capability names that are not in the W3C spec. Spec-compliant
    drivers will reject requests containing unknown capability names.

    Moves the Firefox profile, if present, from the old location to the new Firefox
    options object.

    :Args:
     - caps - A dictionary of capabilities requested by the caller.
    """
    ...

class WebDriver(object):
    """
    Controls a browser by sending commands to a remote server.
    This server is expected to be running the WebDriver wire protocol
    as defined at
    https://github.com/SeleniumHQ/selenium/wiki/JsonWireProtocol

    :Attributes:
     - session_id - String ID of the browser session started and controlled by this WebDriver.
     - capabilities - Dictionaty of effective capabilities of this browser session as returned
         by the remote server. See https://github.com/SeleniumHQ/selenium/wiki/DesiredCapabilities
     - command_executor - remote_connection.RemoteConnection object used to execute commands.
     - error_handler - errorhandler.ErrorHandler object used to handle errors.
    """
    _web_element_cls = ...
    def __init__(self, command_executor=..., desired_capabilities: Optional[Any] = ..., browser_profile: Optional[Any] = ..., proxy: Optional[Any] = ..., keep_alive: bool = ..., file_detector: Optional[Any] = ..., options: Optional[Any] = ...):
        """
        Create a new driver that will issue commands using the wire protocol.

        :Args:
         - command_executor - Either a string representing URL of the remote server or a custom
             remote_connection.RemoteConnection object. Defaults to 'http://127.0.0.1:4444/wd/hub'.
         - desired_capabilities - A dictionary of capabilities to request when
             starting the browser session. Required parameter.
         - browser_profile - A selenium.webdriver.firefox.firefox_profile.FirefoxProfile object.
             Only used if Firefox is requested. Optional.
         - proxy - A selenium.webdriver.common.proxy.Proxy object. The browser session will
             be started with given proxy settings, if possible. Optional.
         - keep_alive - Whether to configure remote_connection.RemoteConnection to use
             HTTP keep-alive. Defaults to False.
         - file_detector - Pass custom file detector object during instantiation. If None,
             then default LocalFileDetector() will be used.
         - options - instance of a driver options.Options class
        """
        self.command_executor = ...
        self.session_id = ...
        self.capabilities = ...
        self.error_handler = ...
        self.file_detector = ...
    
    def __repr__(self):
        ...
    
    def __enter__(self):
        ...
    
    def __exit__(self, *args):
        ...
    
    @contextmanager
    def file_detector_context(self, file_detector_class, *args, **kwargs):
        """
        Overrides the current file detector (if necessary) in limited context.
        Ensures the original file detector is set afterwards.

        Example:

        with webdriver.file_detector_context(UselessFileDetector):
            someinput.send_keys('/etc/hosts')

        :Args:
         - file_detector_class - Class of the desired file detector. If the class is different
             from the current file_detector, then the class is instantiated with args and kwargs
             and used as a file detector during the duration of the context manager.
         - args - Optional arguments that get passed to the file detector class during
             instantiation.
         - kwargs - Keyword arguments, passed the same way as args.
        """
        ...
    
    @property
    def mobile(self):
        ...
    
    @property
    def name(self):
        """Returns the name of the underlying browser for this instance.

        :Usage:
            name = driver.name
        """
        ...
    
    def start_client(self):
        """
        Called before starting a new session. This method may be overridden
        to define custom startup behavior.
        """
        ...
    
    def stop_client(self):
        """
        Called after executing a quit command. This method may be overridden
        to define custom shutdown behavior.
        """
        ...
    
    def start_session(self, capabilities, browser_profile: Optional[Any] = ...):
        """
        Creates a new session with the desired capabilities.

        :Args:
         - browser_name - The name of the browser to request.
         - version - Which browser version to request.
         - platform - Which platform to request the browser on.
         - javascript_enabled - Whether the new session should support JavaScript.
         - browser_profile - A selenium.webdriver.firefox.firefox_profile.FirefoxProfile object. Only used if Firefox is requested.
        """
        self.session_id = ...
        self.capabilities = ...
        self.w3c = ...
    
    def _wrap_value(self, value):
        ...
    
    def create_web_element(self, element_id):
        """Creates a web element with the specified `element_id`."""
        ...
    
    def _unwrap_value(self, value):
        ...
    
    def execute(self, driver_command, params: Optional[Any] = ...):
        """
        Sends a command to be executed by a command.CommandExecutor.

        :Args:
         - driver_command: The name of the command to execute as a string.
         - params: A dictionary of named parameters to send with the command.

        :Returns:
          The command's JSON response loaded into a dictionary object.
        """
        ...
    
    def get(self, url):
        """
        Loads a web page in the current browser session.
        """
        ...
    
    @property
    def title(self):
        """Returns the title of the current page.

        :Usage:
            title = driver.title
        """
        ...
    
    def find_element_by_id(self, id_):
        """Finds an element by id.

        :Args:
         - id\_ - The id of the element to be found.

        :Returns:
         - WebElement - the element if it was found

        :Raises:
         - NoSuchElementException - if the element wasn't found

        :Usage:
            element = driver.find_element_by_id('foo')
        """
        ...
    
    def find_elements_by_id(self, id_):
        """
        Finds multiple elements by id.

        :Args:
         - id\_ - The id of the elements to be found.

        :Returns:
         - list of WebElement - a list with elements if any was found.  An
           empty list if not

        :Usage:
            elements = driver.find_elements_by_id('foo')
        """
        ...
    
    def find_element_by_xpath(self, xpath):
        """
        Finds an element by xpath.

        :Args:
         - xpath - The xpath locator of the element to find.

        :Returns:
         - WebElement - the element if it was found

        :Raises:
         - NoSuchElementException - if the element wasn't found

        :Usage:
            element = driver.find_element_by_xpath('//div/td[1]')
        """
        ...
    
    def find_elements_by_xpath(self, xpath):
        """
        Finds multiple elements by xpath.

        :Args:
         - xpath - The xpath locator of the elements to be found.

        :Returns:
         - list of WebElement - a list with elements if any was found.  An
           empty list if not

        :Usage:
            elements = driver.find_elements_by_xpath("//div[contains(@class, 'foo')]")
        """
        ...
    
    def find_element_by_link_text(self, link_text):
        """
        Finds an element by link text.

        :Args:
         - link_text: The text of the element to be found.

        :Returns:
         - WebElement - the element if it was found

        :Raises:
         - NoSuchElementException - if the element wasn't found

        :Usage:
            element = driver.find_element_by_link_text('Sign In')
        """
        ...
    
    def find_elements_by_link_text(self, text):
        """
        Finds elements by link text.

        :Args:
         - link_text: The text of the elements to be found.

        :Returns:
         - list of webelement - a list with elements if any was found.  an
           empty list if not

        :Usage:
            elements = driver.find_elements_by_link_text('Sign In')
        """
        ...
    
    def find_element_by_partial_link_text(self, link_text):
        """
        Finds an element by a partial match of its link text.

        :Args:
         - link_text: The text of the element to partially match on.

        :Returns:
         - WebElement - the element if it was found

        :Raises:
         - NoSuchElementException - if the element wasn't found

        :Usage:
            element = driver.find_element_by_partial_link_text('Sign')
        """
        ...
    
    def find_elements_by_partial_link_text(self, link_text):
        """
        Finds elements by a partial match of their link text.

        :Args:
         - link_text: The text of the element to partial match on.

        :Returns:
         - list of webelement - a list with elements if any was found.  an
           empty list if not

        :Usage:
            elements = driver.find_elements_by_partial_link_text('Sign')
        """
        ...
    
    def find_element_by_name(self, name):
        """
        Finds an element by name.

        :Args:
         - name: The name of the element to find.

        :Returns:
         - WebElement - the element if it was found

        :Raises:
         - NoSuchElementException - if the element wasn't found

        :Usage:
            element = driver.find_element_by_name('foo')
        """
        ...
    
    def find_elements_by_name(self, name):
        """
        Finds elements by name.

        :Args:
         - name: The name of the elements to find.

        :Returns:
         - list of webelement - a list with elements if any was found.  an
           empty list if not

        :Usage:
            elements = driver.find_elements_by_name('foo')
        """
        ...
    
    def find_element_by_tag_name(self, name):
        """
        Finds an element by tag name.

        :Args:
         - name - name of html tag (eg: h1, a, span)

        :Returns:
         - WebElement - the element if it was found

        :Raises:
         - NoSuchElementException - if the element wasn't found

        :Usage:
            element = driver.find_element_by_tag_name('h1')
        """
        ...
    
    def find_elements_by_tag_name(self, name):
        """
        Finds elements by tag name.

        :Args:
         - name - name of html tag (eg: h1, a, span)

        :Returns:
         - list of WebElement - a list with elements if any was found.  An
           empty list if not

        :Usage:
            elements = driver.find_elements_by_tag_name('h1')
        """
        ...
    
    def find_element_by_class_name(self, name):
        """
        Finds an element by class name.

        :Args:
         - name: The class name of the element to find.

        :Returns:
         - WebElement - the element if it was found

        :Raises:
         - NoSuchElementException - if the element wasn't found

        :Usage:
            element = driver.find_element_by_class_name('foo')
        """
        ...
    
    def find_elements_by_class_name(self, name):
        """
        Finds elements by class name.

        :Args:
         - name: The class name of the elements to find.

        :Returns:
         - list of WebElement - a list with elements if any was found.  An
           empty list if not

        :Usage:
            elements = driver.find_elements_by_class_name('foo')
        """
        ...
    
    def find_element_by_css_selector(self, css_selector):
        """
        Finds an element by css selector.

        :Args:
         - css_selector - CSS selector string, ex: 'a.nav#home'

        :Returns:
         - WebElement - the element if it was found

        :Raises:
         - NoSuchElementException - if the element wasn't found

        :Usage:
            element = driver.find_element_by_css_selector('#foo')
        """
        ...
    
    def find_elements_by_css_selector(self, css_selector):
        """
        Finds elements by css selector.

        :Args:
         - css_selector - CSS selector string, ex: 'a.nav#home'

        :Returns:
         - list of WebElement - a list with elements if any was found.  An
           empty list if not

        :Usage:
            elements = driver.find_elements_by_css_selector('.foo')
        """
        ...
    
    def execute_script(self, script, *args):
        """
        Synchronously Executes JavaScript in the current window/frame.

        :Args:
         - script: The JavaScript to execute.
         - \*args: Any applicable arguments for your JavaScript.

        :Usage:
            driver.execute_script('return document.title;')
        """
        ...
    
    def execute_async_script(self, script, *args):
        """
        Asynchronously Executes JavaScript in the current window/frame.

        :Args:
         - script: The JavaScript to execute.
         - \*args: Any applicable arguments for your JavaScript.

        :Usage:
            script = "var callback = arguments[arguments.length - 1]; " \
                     "window.setTimeout(function(){ callback('timeout') }, 3000);"
            driver.execute_async_script(script)
        """
        ...
    
    @property
    def current_url(self):
        """
        Gets the URL of the current page.

        :Usage:
            driver.current_url
        """
        ...
    
    @property
    def page_source(self):
        """
        Gets the source of the current page.

        :Usage:
            driver.page_source
        """
        ...
    
    def close(self):
        """
        Closes the current window.

        :Usage:
            driver.close()
        """
        ...
    
    def quit(self):
        """
        Quits the driver and closes every associated window.

        :Usage:
            driver.quit()
        """
        ...
    
    @property
    def current_window_handle(self):
        """
        Returns the handle of the current window.

        :Usage:
            driver.current_window_handle
        """
        ...
    
    @property
    def window_handles(self):
        """
        Returns the handles of all windows within the current session.

        :Usage:
            driver.window_handles
        """
        ...
    
    def maximize_window(self):
        """
        Maximizes the current window that webdriver is using
        """
        ...
    
    def fullscreen_window(self):
        """
        Invokes the window manager-specific 'full screen' operation
        """
        ...
    
    def minimize_window(self):
        """
        Invokes the window manager-specific 'minimize' operation
        """
        ...
    
    @property
    def switch_to(self):
        """
        :Returns:
            - SwitchTo: an object containing all options to switch focus into

        :Usage:
            element = driver.switch_to.active_element
            alert = driver.switch_to.alert
            driver.switch_to.default_content()
            driver.switch_to.frame('frame_name')
            driver.switch_to.frame(1)
            driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0])
            driver.switch_to.parent_frame()
            driver.switch_to.window('main')
        """
        ...
    
    def switch_to_active_element(self):
        """ Deprecated use driver.switch_to.active_element
        """
        ...
    
    def switch_to_window(self, window_name):
        """ Deprecated use driver.switch_to.window
        """
        ...
    
    def switch_to_frame(self, frame_reference):
        """ Deprecated use driver.switch_to.frame
        """
        ...
    
    def switch_to_default_content(self):
        """ Deprecated use driver.switch_to.default_content
        """
        ...
    
    def switch_to_alert(self):
        """ Deprecated use driver.switch_to.alert
        """
        ...
    
    def back(self):
        """
        Goes one step backward in the browser history.

        :Usage:
            driver.back()
        """
        ...
    
    def forward(self):
        """
        Goes one step forward in the browser history.

        :Usage:
            driver.forward()
        """
        ...
    
    def refresh(self):
        """
        Refreshes the current page.

        :Usage:
            driver.refresh()
        """
        ...
    
    def get_cookies(self):
        """
        Returns a set of dictionaries, corresponding to cookies visible in the current session.

        :Usage:
            driver.get_cookies()
        """
        ...
    
    def get_cookie(self, name):
        """
        Get a single cookie by name. Returns the cookie if found, None if not.

        :Usage:
            driver.get_cookie('my_cookie')
        """
        ...
    
    def delete_cookie(self, name):
        """
        Deletes a single cookie with the given name.

        :Usage:
            driver.delete_cookie('my_cookie')
        """
        ...
    
    def delete_all_cookies(self):
        """
        Delete all cookies in the scope of the session.

        :Usage:
            driver.delete_all_cookies()
        """
        ...
    
    def add_cookie(self, cookie_dict):
        """
        Adds a cookie to your current session.

        :Args:
         - cookie_dict: A dictionary object, with required keys - "name" and "value";
            optional keys - "path", "domain", "secure", "expiry"

        Usage:
            driver.add_cookie({'name' : 'foo', 'value' : 'bar'})
            driver.add_cookie({'name' : 'foo', 'value' : 'bar', 'path' : '/'})
            driver.add_cookie({'name' : 'foo', 'value' : 'bar', 'path' : '/', 'secure':True})

        """
        ...
    
    def implicitly_wait(self, time_to_wait):
        """
        Sets a sticky timeout to implicitly wait for an element to be found,
           or a command to complete. This method only needs to be called one
           time per session. To set the timeout for calls to
           execute_async_script, see set_script_timeout.

        :Args:
         - time_to_wait: Amount of time to wait (in seconds)

        :Usage:
            driver.implicitly_wait(30)
        """
        ...
    
    def set_script_timeout(self, time_to_wait):
        """
        Set the amount of time that the script should wait during an
           execute_async_script call before throwing an error.

        :Args:
         - time_to_wait: The amount of time to wait (in seconds)

        :Usage:
            driver.set_script_timeout(30)
        """
        ...
    
    def set_page_load_timeout(self, time_to_wait):
        """
        Set the amount of time to wait for a page load to complete
           before throwing an error.

        :Args:
         - time_to_wait: The amount of time to wait

        :Usage:
            driver.set_page_load_timeout(30)
        """
        ...
    
    def find_element(self, by=..., value: Optional[Any] = ...):
        """
        Find an element given a By strategy and locator. Prefer the find_element_by_* methods when
        possible.

        :Usage:
            element = driver.find_element(By.ID, 'foo')

        :rtype: WebElement
        """
        ...
    
    def find_elements(self, by=..., value: Optional[Any] = ...):
        """
        Find elements given a By strategy and locator. Prefer the find_elements_by_* methods when
        possible.

        :Usage:
            elements = driver.find_elements(By.CLASS_NAME, 'foo')

        :rtype: list of WebElement
        """
        ...
    
    @property
    def desired_capabilities(self):
        """
        returns the drivers current desired capabilities being used
        """
        ...
    
    def get_screenshot_as_file(self, filename):
        """
        Saves a screenshot of the current window to a PNG image file. Returns
           False if there is any IOError, else returns True. Use full paths in
           your filename.

        :Args:
         - filename: The full path you wish to save your screenshot to. This
           should end with a `.png` extension.

        :Usage:
            driver.get_screenshot_as_file('/Screenshots/foo.png')
        """
        ...
    
    def save_screenshot(self, filename):
        """
        Saves a screenshot of the current window to a PNG image file. Returns
           False if there is any IOError, else returns True. Use full paths in
           your filename.

        :Args:
         - filename: The full path you wish to save your screenshot to. This
           should end with a `.png` extension.

        :Usage:
            driver.save_screenshot('/Screenshots/foo.png')
        """
        ...
    
    def get_screenshot_as_png(self):
        """
        Gets the screenshot of the current window as a binary data.

        :Usage:
            driver.get_screenshot_as_png()
        """
        ...
    
    def get_screenshot_as_base64(self):
        """
        Gets the screenshot of the current window as a base64 encoded string
           which is useful in embedded images in HTML.

        :Usage:
            driver.get_screenshot_as_base64()
        """
        ...
    
    def set_window_size(self, width, height, windowHandle=...):
        """
        Sets the width and height of the current window. (window.resizeTo)

        :Args:
         - width: the width in pixels to set the window to
         - height: the height in pixels to set the window to

        :Usage:
            driver.set_window_size(800,600)
        """
        ...
    
    def get_window_size(self, windowHandle=...):
        """
        Gets the width and height of the current window.

        :Usage:
            driver.get_window_size()
        """
        ...
    
    def set_window_position(self, x, y, windowHandle=...):
        """
        Sets the x,y position of the current window. (window.moveTo)

        :Args:
         - x: the x-coordinate in pixels to set the window position
         - y: the y-coordinate in pixels to set the window position

        :Usage:
            driver.set_window_position(0,0)
        """
        ...
    
    def get_window_position(self, windowHandle=...):
        """
        Gets the x,y position of the current window.

        :Usage:
            driver.get_window_position()
        """
        ...
    
    def get_window_rect(self):
        """
        Gets the x, y coordinates of the window as well as height and width of
        the current window.

        :Usage:
            driver.get_window_rect()
        """
        ...
    
    def set_window_rect(self, x: Optional[Any] = ..., y: Optional[Any] = ..., width: Optional[Any] = ..., height: Optional[Any] = ...):
        """
        Sets the x, y coordinates of the window as well as height and width of
        the current window.

        :Usage:
            driver.set_window_rect(x=10, y=10)
            driver.set_window_rect(width=100, height=200)
            driver.set_window_rect(x=10, y=10, width=100, height=200)
        """
        ...
    
    @property
    def file_detector(self):
        ...
    
    @file_detector.setter
    def file_detector(self, detector):
        """
        Set the file detector to be used when sending keyboard input.
        By default, this is set to a file detector that does nothing.

        see FileDetector
        see LocalFileDetector
        see UselessFileDetector

        :Args:
         - detector: The detector to use. Must not be None.
        """
        ...
    
    @property
    def orientation(self):
        """
        Gets the current orientation of the device

        :Usage:
            orientation = driver.orientation
        """
        ...
    
    @orientation.setter
    def orientation(self, value):
        """
        Sets the current orientation of the device

        :Args:
         - value: orientation to set it to.

        :Usage:
            driver.orientation = 'landscape'
        """
        ...
    
    @property
    def application_cache(self):
        """ Returns a ApplicationCache Object to interact with the browser app cache"""
        ...
    
    @property
    def log_types(self):
        """
        Gets a list of the available log types

        :Usage:
            driver.log_types
        """
        ...
    
    def get_log(self, log_type):
        """
        Gets the log for a given log type

        :Args:
         - log_type: type of log that which will be returned

        :Usage:
            driver.get_log('browser')
            driver.get_log('driver')
            driver.get_log('client')
            driver.get_log('server')
        """
        ...
    


