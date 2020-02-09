"""
This type stub file was generated by pyright.
"""

class Select(object):
    def __init__(self, webelement):
        """
        Constructor. A check is made that the given element is, indeed, a SELECT tag. If it is not,
        then an UnexpectedTagNameException is thrown.

        :Args:
         - webelement - element SELECT element to wrap

        Example:
            from selenium.webdriver.support.ui import Select \n
            Select(driver.find_element_by_tag_name("select")).select_by_index(2)
        """
        self.is_multiple = ...
    
    @property
    def options(self):
        """Returns a list of all options belonging to this select tag"""
        ...
    
    @property
    def all_selected_options(self):
        """Returns a list of all selected options belonging to this select tag"""
        ...
    
    @property
    def first_selected_option(self):
        """The first selected option in this select tag (or the currently selected option in a
        normal select)"""
        ...
    
    def select_by_value(self, value):
        """Select all options that have a value matching the argument. That is, when given "foo" this
           would select an option like:

           <option value="foo">Bar</option>

           :Args:
            - value - The value to match against

           throws NoSuchElementException If there is no option with specisied value in SELECT
           """
        ...
    
    def select_by_index(self, index):
        """Select the option at the given index. This is done by examing the "index" attribute of an
           element, and not merely by counting.

           :Args:
            - index - The option at this index will be selected

           throws NoSuchElementException If there is no option with specisied index in SELECT
           """
        ...
    
    def select_by_visible_text(self, text):
        """Select all options that display text matching the argument. That is, when given "Bar" this
           would select an option like:

            <option value="foo">Bar</option>

           :Args:
            - text - The visible text to match against

            throws NoSuchElementException If there is no option with specisied text in SELECT
           """
        ...
    
    def deselect_all(self):
        """Clear all selected entries. This is only valid when the SELECT supports multiple selections.
           throws NotImplementedError If the SELECT does not support multiple selections
        """
        ...
    
    def deselect_by_value(self, value):
        """Deselect all options that have a value matching the argument. That is, when given "foo" this
           would deselect an option like:

            <option value="foo">Bar</option>

           :Args:
            - value - The value to match against

            throws NoSuchElementException If there is no option with specisied value in SELECT
        """
        ...
    
    def deselect_by_index(self, index):
        """Deselect the option at the given index. This is done by examing the "index" attribute of an
           element, and not merely by counting.

           :Args:
            - index - The option at this index will be deselected

            throws NoSuchElementException If there is no option with specisied index in SELECT
        """
        ...
    
    def deselect_by_visible_text(self, text):
        """Deselect all options that display text matching the argument. That is, when given "Bar" this
           would deselect an option like:

           <option value="foo">Bar</option>

           :Args:
            - text - The visible text to match against
        """
        ...
    
    def _setSelected(self, option):
        ...
    
    def _unsetSelected(self, option):
        ...
    
    def _escapeString(self, value):
        ...
    
    def _get_longest_token(self, value):
        ...
    

