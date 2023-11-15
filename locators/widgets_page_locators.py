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

class DatePickerPageLocators:

    DATE_INPUT = (By.CSS_SELECTOR, "input[id='datePickerMonthYearInput']")
    DATE_SELECT_MONTH = (By.CSS_SELECTOR, "select[class ='react-datepicker__month-select']")
    DATE_SELECT_YEAR = (By.CSS_SELECTOR, "select[class ='react-datepicker__year-select']")
    DATE_SELECT_DAY_LIST = (By.CSS_SELECTOR, "div[class^='react-datepicker__day react-datepicker__day']")

    DATE_AND_TIME_INPUT = (By.CSS_SELECTOR, "input[id='dateAndTimePickerInput']")
    DATE_AND_TIME_MONTH = (By.CSS_SELECTOR, "div[class='react-datepicker__month-read-view']")
    DATE_AND_TIME_YEAR = (By.CSS_SELECTOR, "div[class='react-datepicker__year-read-view']")
    DATE_AND_TIME_TIME_LIST = (By.CSS_SELECTOR, "li[class='react-datepicker__time-list-item ']")
    DATE_AND_TIME_MONTH_LIST = (By.CSS_SELECTOR, "div[class='react-datepicker__month-option']")
    DATE_AND_TIME_YEAR_LIST = (By.CSS_SELECTOR, "div[class='react-datepicker__year-option']")

class SliderPageLocators:
    
    INPUT_SLIDER = (By.CSS_SELECTOR, "input[class='range-slider range-slider--primary']")
    SLIDER_VALUE = (By.CSS_SELECTOR, "input[id='sliderValue']") 

class ProgressBarPageLocators:
    PROGRESS_BAR_BUTTON = (By.CSS_SELECTOR, "button[id='startStopButton']")
    PROGRESS_BAR_VALUE = (By.CSS_SELECTOR, "div[class='progress-bar bg-info']")

class TabsPageLocators:
    TABS_WHAT = (By.CSS_SELECTOR, "a[id='demo-tab-what']")
    TABS_WHAT_CONTENT = (By.CSS_SELECTOR, "div[id='demo-tabpane-what']")
    TABS_ORIGIN = (By.CSS_SELECTOR, "a[id='demo-tab-origin']")
    TABS_ORIGIN_CONTENT = (By.CSS_SELECTOR, "div[id='demo-tabpane-origin']")
    TABS_USE = (By.CSS_SELECTOR, "a[id='demo-tab-use']")
    TABS_USE_CONTENT = (By.CSS_SELECTOR, "div[id='demo-tabpane-use']")
    TABS_MORE = (By.CSS_SELECTOR, "a[id='demo-tab-more']")
    TABS_MORE_CONTENT = (By.CSS_SELECTOR, "div[id='demo-tabpane-more']")

class ToolTipsPageLocators:

    BUTTON = (By.CSS_SELECTOR, "button[id='toolTipButton']")
    TOOL_TIP_BUTTON = (By.CSS_SELECTOR, "button[aria-describedby='buttonToolTip']")
    
    FIELD = (By.CSS_SELECTOR, "div[id='texFieldToolTopContainer'] input")
    TOOL_TIP_FIELD = (By.CSS_SELECTOR, "input[aria-describedby='textFieldToolTip']")
    
    CONTARY_LINK = (By.XPATH, "//*[@id='texToolTopContainer']/a[1]")
    TOOL_TIP_CONTARY_LINK= (By.CSS_SELECTOR, "a[aria-describedby='contraryTexToolTip']")
    
    SECTION_LINK = (By.XPATH, "//*[@id='texToolTopContainer']/a[2]")
    TOOL_TIP_SECTION_LINK = (By.CSS_SELECTOR, "a[aria-describedby='sectionToolTip']")

    TOOL_TIPS_INNERS = (By.CSS_SELECTOR, "div[class='tooltip-inner']")