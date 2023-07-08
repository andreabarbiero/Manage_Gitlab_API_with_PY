import requests

gitlab_url = "https://SOSTITUIRE_GITLAB_URL/api/v4"  # Aggiorna con l'URL del tuo GitLab CE
access_token = "TOKEN_CON_PERMESSI_API"  # Aggiorna con il tuo token di accesso

csv_file = "users.csv"

with open(csv_file, newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        username = row['username']
        email = row['email']
        password = row['password']


      # Creazione dell'utente
      user_endpoint = f"{gitlab_url}/users"
      headers = {
          "Private-Token": access_token,
          "Content-Type": "application/json"
      }
      user_data = {
          "username": username,
          "password": password,
          "email": email,
          "name": username,  
          "skip_confirmation": True
      }

      user_response = requests.post(user_endpoint, headers=headers, json=user_data)

      if user_response.status_code == 201:
          print(f"Utente {username} creato con successo.")
      else:
          print(f"Errore durante la creazione dell'utente {username}: {user_response.text}")
          continue

      # Impostazione del flag "password_automatically_set" per il primo accesso
      user_id = user_response.json()["id"]
      user_update_endpoint = f"{gitlab_url}/users/{user_id}"
      user_update_data = {
          "password_automatically_set": True
      }

      user_update_response = requests.put(user_update_endpoint, headers=headers, json=user_update_data)

      if user_update_response.status_code == 200:
          print(f"Impostato il flag 'password_automatically_set' per l'utente {username}.")
      else:
          print(f"Errore durante l'impostazione del flag 'password_automatically_set' per l'utente {username}: {user_update_response.text}")
    
