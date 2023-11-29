# Momozzi Server

## How To Start

1. **Install Dependencies**: Run `pip install -r requirements.txt` to install required packages.
2. **Environment Variables**: Rename `.env.example` to `.env` and update the values as needed.
3. **Database Setup**: Create a schema named "momozzi" in MySQL.
4. **Migrations**: Run `python manage.py makemigrations` to create migration files.
5. **Apply Migrations**: Run `python manage.py migrate` to apply migrations to the database.
6. **Start Server**: Run `python manage.py runserver {port number}` to start the Django server.

## Endpoints

### User
- **GET /api/user/**: Retrieve all users.
- **GET /api/user/{user_id}**: Get a specific user by ID.
- **POST /api/user/**: Add a new user (send `user_id`, `first_name`, `last_name`, and `age` in request body).
- **DELETE /api/user/**: Delete a user (send `user_id` in request body).
- **PUT /api/user/**: Update a user (send `user_id`, `first_name`, `last_name`, and `age` in request body).

### Cuisine
- **GET /api/cuisine/**: Retrieve all cuisines.
- **GET /api/cuisine/{cuisine_name}**: Get a specific cuisine by name.
- **POST /api/cuisine/**: Add a new cuisine (send `cuisine_name`, `method`, and `category` in request body).
- **DELETE /api/cuisine/**: Delete a cuisine (send `cuisine_name` in request body).
- **PUT /api/cuisine/**: Update a cuisine (send `cuisine_name`, `method`, and `category` in request body).

### Recipe
- **GET /api/recipe/**: Retrieve all recipes.
- **GET /api/recipe/{recipe_id}**: Get a specific recipe by ID.
- **POST /api/recipe/**: Add a new recipe (send `recipe_id`, `cook_time`, `description`, `process`, and `cuisine_name` in request body).
- **DELETE /api/recipe/**: Delete a recipe (send `recipe_id` in request body).
- **PUT /api/recipe/**: Update a recipe (send `recipe_id`, `cook_time`, `description`, `process`, and `cuisine_name` in request body).

### Ingredient
- **GET /api/ingredient/**: Retrieve all ingredients.
- **GET /api/ingredient/{ingredient_name}**: Get a specific ingredient by name.
- **POST /api/ingredient/**: Add a new ingredient (send `ingredient_name`, `type`, and `calories` in request body).
- **DELETE /api/ingredient/**: Delete an ingredient (send `ingredient_name` in request body).
- **PUT /api/ingredient/**: Update an ingredient (send `ingredient_name`, `type`, and `calories` in request body).

### Review
- **GET /api/review/**: Retrieve all reviews.
- **GET /api/review/{review_id}**: Get a specific review by ID.
- **POST /api/review/**: Add a new review (send `review_id`, `content`, `user_id`, and `recipe_id` in request body).
- **DELETE /api/review/**: Delete a review (send `review_id` in request body).
- **PUT /api/review/**: Update a review (send `review_id`, `content`, `user_id`, and `recipe_id` in request body).

### Recipe Needs Ingredient
- **GET /api/recipe_needs_ingredient/**: Retrieve all recipe-ingredient relationships.
- **GET /api/recipe_needs_ingredient/{recipe_id}/{ingredient_name}**: Get a specific recipe-ingredient relationship.
- **POST /api/recipe_needs_ingredient/**: Add a new recipe-ingredient relationship (send `recipe_id` and `ingredient_name` in request body).
- **DELETE /api/recipe_needs_ingredient/**: Delete a recipe-ingredient relationship (send `recipe_id` and `ingredient_name` in request body).
- **PUT /api/recipe_needs_ingredient/**: Update a recipe-ingredient relationship (send `recipe_id` and `ingredient_name` in request body).

### Refrigerator
- **GET /api/refrigerator/**: Retrieve all refrigerators.
- **GET /api/refrigerator/{user_id}/{created_at}**: Get a specific refrigerator by user ID and creation date.
- **POST /api/refrigerator/**: Add a new refrigerator (send `user_id`, `created_at`, and `capacity` in request body).
- **DELETE /api/refrigerator/**: Delete a refrigerator (send `user_id` and `created_at` in request body).
- **PUT /api/refrigerator/**: Update a refrigerator (send `user_id`, `created_at`, and `capacity` in request body).

### Refrigerator Stores Ingredient
- **GET /api/refrigerator_stores_ingredient/**: Retrieve all refrigerator-ingredient relationships.
- **GET /api/refrigerator_stores_ingredient/{refrigerator}/{ingredient_name}**: Get a specific refrigerator-ingredient relationship.
- **POST /api/refrigerator_stores_ingredient/**: Add a new refrigerator-ingredient relationship (send `refrigerator` and `ingredient_name` in request body).
- **DELETE /api/refrigerator_stores_ingredient/**: Delete a refrigerator-ingredient relationship (send `refrigerator` and `ingredient_name` in request body).
- **PUT /api/refrigerator_stores_ingredient/**: Update a refrigerator-ingredient relationship (send `refrigerator` and `ingredient_name` in request body).

### Dummy Data and Clear Data
- **GET /api/dummy/**: Add dummy data to the database.
- **GET /api/clear/**: Clear all data from the database.
