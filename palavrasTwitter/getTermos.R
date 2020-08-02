library(rtweet)
library(dplyr)
library(readr)

# pega o dia da semana, um código de 0 a 6(começa no domingo)
dia <- as.POSIXlt(Sys.Date())$wday

semana <-  list(dom = c('respiradores','medicamento','infectados'),
              seg = c('vacina','máscara','leitos'), 
              ter = c('covid','gripezinha','UTI'), 
              qua = c('quarentena','pandemia','isolamento'),
              qui = c('hospital','recuperados','coronavirus'), 
              sex = c('SARS-CoV-2','vírus','covid-19'),
              sab = c('infectologista','covid19','OMS'))

codigo <-  c(0:6)
df <- as.data.frame(cbind(codigo, semana))

coleta <- df %>% 
  filter(codigo == dia)

resultados <- data.frame(text = character(),
                screen_name = character(), 
                status_id = character(), 
                created_at = as.Date(character())) 

for(i in c(1:length(coleta$semana[[1]]))){
  termo <-  coleta$semana[[1]][i]
  message(termo)
  search <- search_tweets(termo, n = 6000, include_rts = FALSE)
  search <- data.frame(text = search$text, 
                       screen_name = search$screen_name, 
                       status_id = search$status_id, 
                       created_at = search$created_at)
  resultados <- bind_rows(resultados, search)
  if (i != 3){
    Sys.sleep(15*60)
  }
}

write_csv(resultados, "busca_por_palavras.csv")