################################################################################################################################

wants <- c('tidyr','lubridate','tibble','data.table','knitr','caret','boot',
           'ggplot2','gridExtra','pander','ggthemes','scales','foreign','magrittr','reshape2','glmnet',
           'mgcv','cvTools','rpart','class','psych','stringr','rpart.plot',
           'randomForest','corrplot','bit64','dplyr','readxl','openxlsx',
           'stringr','shiny','shinydashboard','shinyWidgets','DT','rhandsontable','shinyMatrix',
           'BBmisc','plotly','rlang','shinyalert','shinymanager')

has <- wants %in% rownames(installed.packages())
if(any(!has))install.packages(wants[!has])
lapply(wants,library, character.only = T)



inactivity <- "function idleTimer()
var t = setTimeout(logout, 1200000);
window.onmousemove = resetTimer;
window.onmousedown = resetTimer;
window.onclick = resetTimer;
window.onscroll = resetTimer;
window.onkeypress = resetTimer;

function logout(){
window.close();
}

function resetTimer(){
clearTimeout(t)；
t = setTimeout(logout,120000);
}
}
idleTimer();
"

credentials <- data.frame(user = c("Jenn"),password = c("hijenn"),
                          stringsAsFactors = FALSE)



ui<-secure_app(head_auth = tags$script(inactivity),
               dashboardPage(skin = "red",
                  dashboardHeader(title = "Charlie Chocolate"),
                  dashboardSidebar(sidebarMenu(
                    menuItem("Dashboard",tabName = "summary",icon = icon('list')),
                    menuItem("Assortment",tabName ="assort",icon = icon('th')),
                    menuItem("Optimization",tabName ="optimization",icon = icon('signal')),
                    menuItem("Performance",tabName ="performance",icon = icon('search')),
                    menuItem("Trade",tabName ="offer",icon = icon('funnel-dollar'))
                  )),
                  dashboardBody(tags$style(HTML('.content-wrapper, .right-side{
                  background-color:#FFFFFF;
                  }')))
  ))


# Define server logic required to draw a histogram
server <- function(input, output) {
   result_auth <-secure_server(check_credentials = check_credentials(credentials))
      
}



# Run the application 
shinyApp(ui = ui, server = server)

