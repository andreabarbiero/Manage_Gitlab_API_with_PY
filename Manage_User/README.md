# GESTIRE GITLAB TRAMITE LE SUE API

Questo script automatizza la creazione di utenti su Gitlab.

Ho modificato lo script in modo tale che prenda la lista utenti ed i dati come email e password da un file CSV,
i campi al momento sono 3 username, email e password ma dato che il profilo utente Gitlab ha molte informazioni, 
e' possibile aggiungere i campi che si vuole, basta aggiungere poi le variabili nella prima for dove viene letto il file CSV.

```shell
  pip3 install requests
  pip3 install csv
```
