# betting
## Для запуска  
```
docker-compose up -d --build
```

## Взаимодействие
**[localhost:8080/docs](localhost:8080/docs) - *line-provider***  
**[localhost:8000/docs](localhost:8000/docs) - *betmaker***  

Перед началом необходимо создать в ```line-provider``` несколько событий. В параметре ```deadline``` указывается время в секундах (```time.time()```)  

После этого создать в ```betmaker``` соответствующие событиям ставки.   

По прошествию дедлайна, через коллбек у ставок будет меняться статус с ```new``` на ```win/lose```.  

