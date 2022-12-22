# Desafio-Latam-2022

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#project-structure">Project structure</a>
    </li>
    <li><a href="#commands">Commands</a></li>
  </ol>
</details>

<!-- PROJECT STRUCTURE -->

### Project structure

    
    ├── model-api                    # Global folder for api app
        ├── app                      # Global setting for app
             ├── controller          # controller, bussiness logic
             ├── routes              # API routes
             ├── services            # Class that connect with models or data services         
        ├── config                   # Config for project, include envs
        ├── models                   # prediction models  and categories for create model input
        ├── schemas                  # Structure classes for data preprocesing, model predict   
        ├── utils                    # Utility classes or functions like: conversors, file manager and others  
        ├── main.py
        └── requirements.txt 
    ├── Notebook                     # Global folder for data analitic and training models
        ├── data          
             └──dataset_SCL.csv
        ├── graphics_functions.py    # functions library for data analitics  
        ├── solution.ipynb              
        ├── synthetic_features.csv  



 Use short lowercase names at least for the top-level files and folders except
 `LICENSE`, `README.md`

<!-- COMMANDS -->

## Commands

All commands:

- Install dependencies

  ```sh
  python3 -m pip install -r requirements.txt
  ```

- Run project api: Desafio-Latam-API-models

  ```sh
  python3 main.py
  ```

