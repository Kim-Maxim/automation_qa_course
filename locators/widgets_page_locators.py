from selenium.webdriver.common.by import By

class AccordianPageLocators:

    SECTION_FIRST = (By.CSS_SELECTOR, "div[id='section1Heading']")
    SECTION_FIRST_CONTENT = (By.CSS_SELECTOR, "div[id='section1Content']")
    SECTION_SECOND = (By.CSS_SELECTOR, "div[id='section2Heading']")
    SECTION_SECOND_CONTENT = (By.CSS_SELECTOR, "div[id='section2Content']")
    SECTION_THIRD = (By.CSS_SELECTOR, "div[id='section3Heading']")
    SECTION_THIRD_CONTENT = (By.CSS_SELECTOR, "div[id='section3Content']")

class AutoCompletePageLocators:
    
    MULTI_INPUT = (By.CSS_SELECTOR, "input[id ='autoCompleteMultipleInput']")
    MULTI_VALUE = (By.CSS_SELECTOR, "div[class ='css-12jo7m5 auto-complete__multi-value__label']")
    MULTI_VALUE_REMOVE = (By.CSS_SELECTOR, "div[class = 'css-xb97g8 auto-complete__multi-value__remove']")
    SIMPLE_VALUE = (By.CSS_SELECTOR, "div[class='auto-complete__single-value css-1uccc91-singleValue']")
    SIMPLE_INPUT = (By.CSS_SELECTOR, "input[id='autoCompleteSingleInput']")