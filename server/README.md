# Momozzi Server

## How To Start

1. **Install Dependencies**: Run `pip install -r requirements.txt` to install required packages.
2. **Environment Variables**: Rename `.env.example` to `.env` and update the values as needed.
3. **Database Setup**: Create a schema named "momozzi" in MySQL.
4. **Migrations**: Run `python manage.py makemigrations` and `python manage.py makemigrations api` to create migration files.
5. **Apply Migrations**: Run `python manage.py migrate` and `python manage.py migrate api` to apply migrations to the database.
6. **Start Server**: Run `python manage.py runserver {port number}` to start the Django server.

## Endpoints

### User
- **GET /api/user/**: Retrieve all users or a specific user by appending `?user_id={user_id}` or `?email={email}` to the URL.
- **POST /api/user/**: Add a new user (`email`, `password`, `first_name`, `last_name`, and `age` in request body).
- **POST /api/user/login/**: Login a user (send `email` and `password` in request body).
- **DELETE /api/user/**: Delete a user (send `user_id` in request body).
- **PUT /api/user/**: Update a user (send `user_id`, `first_name`, `last_name`, and `age` in request body).

### Cuisine
- **GET /api/cuisine/**: Retrieve all cuisines or a specific cuisine by appending `?cuisine_name={cuisine_name}` to the URL.
- **POST /api/cuisine/**: Add a new cuisine (send `cuisine_name`, `method`, and `category` in request body).
- **DELETE /api/cuisine/**: Delete a cuisine (send `cuisine_name` in request body).
- **PUT /api/cuisine/**: Update a cuisine (send `cuisine_name`, `method`, and `category` in request body).

### Recipe
- **GET /api/recipe/**: Retrieve all recipes or a specific recipe by appending `?recipe_id={recipe_id}` or `?cuisine_name={cuisine_name}` to the URL.
- **GET /api/recipe/keyword/**: Search for recipes by keyword (append `?keyword={keyword}` to the URL).
- **GET /api/recipe/filter/**: Filter recipes by cuisine (append `?method={method}`, `category={category}`, and `ingredient={ingredient}` to the URL).
- **GET /api/recipe/recommend/**: Recommend recipes to a user (append `?refrigerator={refrigerator_id}` to the URL).
- **GET /api/recipe/top/**: Retrieve top 3 recipes by review count.
- **GET /api/recipe/fast/**: Retrieve top 5 recipes by cook time.
- **POST /api/recipe/**: Add a new recipe (`cook_time`, `description`, `process`, and `cuisine_name` in request body).
- **DELETE /api/recipe/**: Delete a recipe (send `recipe_id` in request body).
- **PUT /api/recipe/**: Update a recipe (send `recipe_id`, `cook_time`, `description`, `process`, and `cuisine_name` in request body).

### Ingredient
- **GET /api/ingredient/**: Retrieve all ingredients or a specific ingredient by appending `?ingredient_name={ingredient_name}` to the URL.
- **POST /api/ingredient/**: Add a new ingredient (send `ingredient_name`, `type`, and `calories` in request body).
- **DELETE /api/ingredient/**: Delete an ingredient (send `ingredient_name` in request body).
- **PUT /api/ingredient/**: Update an ingredient (send `ingredient_name`, `type`, and `calories` in request body).

### Review
- **GET /api/review/**: Retrieve all reviews or a specific review by appending `?review_id={review_id}` or `recipe_id={recipe_id}` to the URL.
- **POST /api/review/**: Add a new review (`content`, `user_id`, and `recipe_id` in request body).
- **DELETE /api/review/**: Delete a review (send `review_id` in request body).
- **PUT /api/review/**: Update a review (send `review_id`, `content`, `user_id`, and `recipe_id` in request body).

### Recipe Needs Ingredient
- **GET /api/recipe_needs_ingredient/**: Retrieve all recipe-ingredient relationships or specific ones by appending `?recipe_id={recipe_id}&ingredient_name={ingredient_name}` to the URL.
- **POST /api/recipe_needs_ingredient/**: Add a new recipe-ingredient relationship (send `recipe_id` and `ingredient_name` in request body).
- **DELETE /api/recipe_needs_ingredient/**: Delete a recipe-ingredient relationship (send `recipe_id` and `ingredient_name` in request body).
- **PUT /api/recipe_needs_ingredient/**: Update a recipe-ingredient relationship (send `recipe_id` and `ingredient_name` in request body).

### Refrigerator
- **GET /api/refrigerator/**: Retrieve all refrigerators or a specific refrigerator by appending `?user_id={user_id}` to the URL.
- **POST /api/refrigerator/**: Add a new refrigerator (send `user_id`, `created_at`, and `capacity` in request body).
- **DELETE /api/refrigerator/**: Delete a refrigerator (send `user_id` and `created_at` in request body).
- **PUT /api/refrigerator/**: Update a refrigerator (send `user_id`, `created_at`, and `capacity` in request body).

### Refrigerator Stores Ingredient
- **GET /api/refrigerator_stores_ingredient/**: Retrieve all refrigerator-ingredient relationships or a specific relationship by appending `?refrigerator={refrigerator}&ingredient_name={ingredient_name}` to the URL.
- **POST /api/refrigerator_stores_ingredient/**: Add a new refrigerator-ingredient relationship (send `refrigerator` and `ingredient_name` in request body).
- **DELETE /api/refrigerator_stores_ingredient/**: Delete a refrigerator-ingredient relationship (send `refrigerator` and `ingredient_name` in request body).
- **PUT /api/refrigerator_stores_ingredient/**: Update a refrigerator-ingredient relationship (send `refrigerator` and `ingredient_name` in request body).

### User Likes Cuisine
- **GET /api/user_likes_cuisine/**: Retrieve all user-cuisine relationships or a specific relationship by appending `?user_id={user_id}` to the URL.
- **POST /api/user_likes_cuisine/**: Add a new user-cuisine relationship (send `user_id` and `cuisine_name` in request body).
- **DELETE /api/user_likes_cuisine/**: Delete a user-cuisine relationship (send `user_id` and `cuisine_name` in request body).
- **PUT /api/user_likes_cuisine/**: Update a user-cuisine relationship (send `user_id` and `cuisine_name` in request body).

### Dummy Data and Clear Data
- **GET /api/dummy/**: Add dummy data to the database.
- **GET /api/clear/**: Clear all data from the database.
