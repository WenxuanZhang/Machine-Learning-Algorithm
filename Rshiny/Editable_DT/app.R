#
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

library(shiny)
library(DT)

tableUI <- function(id) {
  ns <- NS(id)
  tagList(
    DTOutput(ns("button")))
}
tableServer<-function(id,data){
  moduleServer(id,
               function(input, output, session){
                 if(!is.null(data)){
                  output$button <- renderDT(datatable(data))
                 }
               }
)
}


# Define UI for application that draws a histogram
ui <- fluidPage(
   
   # Application title
  fluidPage(
    fluidRow(tableUI('test'))
  )
  
)

# Define server logic required to draw a histogram
server <- function(input, output) {
  tableServer('test',iris)
   
}

# Run the application 
shinyApp(ui = ui, server = server)

