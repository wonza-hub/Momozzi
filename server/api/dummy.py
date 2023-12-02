from django.db import connection

def dummy_user_add():
    user_data = [
        {"user_id": 1, "first_name": "홍", "last_name": "길동", "email": "gildong@a.com", "password": "1234", "age": 20},
        {"user_id": 2, "first_name": "김", "last_name": "철수", "email": "kimm@a.com", "password": "1234", "age": 22},
        {"user_id": 3, "first_name": "허", "last_name": "원일", "email": "heo@a.com", "password": "1234", "age": 25},
        {"user_id": 4, "first_name": "박", "last_name": "장고", "email": "django@a.com", "password": "1234", "age": 30},
    ]
    sql = "INSERT INTO api_user (user_id, first_name, last_name, email, password, age) VALUES (%s, %s, %s, %s, %s, %s)"
    with connection.cursor() as cursor:
        for user in user_data:
            cursor.execute(sql, [user['user_id'], user['first_name'], user['last_name'], user['email'], user['password'], user['age']])
    return
    

def dummy_cuisine_add():
    cuisine_data = [
        {"cuisine_name": "치즈계란찜", "method": "찜", "category": "밑반찬"},
        {"cuisine_name": "김치찌개", "method": "끓임", "category": "찌개"},
        {"cuisine_name": "돼지갈비", "method": "굽기", "category": "메인반찬"},
        {"cuisine_name": "일본식 라면", "method": "끓임", "category": "면"},
        {"cuisine_name": "볶음밥", "method": "볶음", "category": "밥"},
        {"cuisine_name": "비빔밥", "method": "비빔", "category": "밥"},
        {"cuisine_name": "스무디", "method": "기타", "category": "디저트"},
        {"cuisine_name": "케이크", "method": "굽기", "category": "디저트"},
    ]
    sql = "INSERT INTO api_cuisine (cuisine_name, method, category) VALUES (%s, %s, %s)"
    with connection.cursor() as cursor:
        for cuisine in cuisine_data:
            cursor.execute(sql, [cuisine['cuisine_name'], cuisine['method'], cuisine['category']])
    return

def dummy_recipe_add():
    recipe_data = [
        {
        "recipe_id": 1,
        "cook_time": 15,
        "description": "집에서 해먹는 일본식 라멘",
        "process": "팬에 오일을 살짝만 두르고 돼지고기 간 것과 간 생강을 넣고 볶는다. 두반장, 미소, 설탕을 넣고, 물 1/4컵을 붓고 조린다. 냄비에 참기름을 두르고 마늘, 생강 1/2t 을 볶는다. 물 400ml, 치킨 부이용 1t, 미소 1T를 넣어 잘 풀어준다. 면을 2분 삶아 넣어준다. 옥수수, 대파, 아지츠케 타마고, 고기, 숙주를 토핑한다. ",
        "cuisine_name": "일본식 라면"
        },
        {
        "recipe_id": 2,
        "cook_time": 7,
        "description": "백종원 7분 김치찌개",
        "process": "목살, 돼지고기, 파를 먹기 좋은 크기로 손질한다. 돼지고기 목살을 한줌(150g) 넣어준다. 물 또는 쌀뜨물 700ml를 냄비에 넣고 준비한 고기와 된장 1/2T를 넣고 끓인다. 적당히 끓인후 김치 (2~3줌)와 다진마늘을 넣고 더 끓인다. 고추가루 1T, 국간장 1T를 넣는다. 소금 또는 새우젓으로 간을 한후 대파를 넣는다. ",
        "cuisine_name": "김치찌개"
        },
        {
        "recipe_id": 3,
        "cook_time": 120,
        "description": "돼지갈비 황금레시피!!",
        "process": "돼지고기(1kg)의 핏물을 뺀 후 잔칼집을 내준다. 간장5Ts, 설탕2Ts, 물엿1Ts, 간마늘1Ts, 참기름1Ts, 배1/4개, 사과1/4개, 매실청1Ts, 대파1뿌리, 물2컵, 깨소금1Ts 을 넣어 양념장을 만든다. 고기를 양념장에 넣고 2시간 이상 재어준다. 고기를 약한불에 굽는다. ",
        "cuisine_name": "돼지갈비"
        },
        {
        "recipe_id": 4,
        "cook_time": 10,
        "description": "누구나 좋아하는 치즈 계란찜!",
        "process": "계란 3개를 깨서 뚝배기에 담는다. 다진 당근 2T, 다진양파 2T, 맛소금 1티스푼, 물 종이컵 1컵, 피자치즈 1줌을 넣어 잘 섞은후 약한 불에 익혀준다. 계란찜의 겉 테두리가 익고 기포가 올라오면 계란찜 위로 피자치즈를 1~2줌 넣어준다. 조금 더 익히면 완성!",
        "cuisine_name": "치즈계란찜"
        },
        {
        "recipe_id": 5,
        "cook_time": 10,
        "description": "10분이면 완성하는 중국식 볶음밥!",
        "process": "햄, 양파, 대파, 당근 을 먹기 좋은 크기로 자른다. 계란 2개를 풀어준다. 웍에 기름은 두르고 햄을 넣고 볶는다. 햄이 노릇해지면 대파를 넣고 볶은후 따로 담아둔다. 웍에 계란을 두르고 휘저어 준다. 계란 위에 밥을 올리고 잘 섞이도록 볶아준다. 간장과 소금으로 간은 해준다. 당근과 새우, 양파를 넣고 볶아준다. 햄과 대파를 넣고 섞어준다. ",
        "cuisine_name": "볶음밥"
        },
        {
        "recipe_id": 6,
        "cook_time": 10,
        "description": "대한민국 전동 비빔밥 만들기!",
        "process": "돼지고기, 양파, 당근, 애호박을 채썰어 준비한다. 고추장 2T, 간장 2T, 설탕 1.5T, 소금 1T, 참기름 1T, 식초 1T 를 넣고 잘섞어 양념장을 만든다. 당근, 애호박 순으로 소금을 한 꼬집씩 넣어 같이 볶아준다. 양파는 간장으로 간을 하며 따로 볶아준다. 돼지고기는 소금, 후추고 간을 하며 따로 볶아준다. 익은 돼지고기를 양념장과 썩은후 밥위에 볶은 야채와 계란후라이와 함께 올려준다.",
        "cuisine_name": "비빔밥"
        },
        {
        "recipe_id": 7,
        "cook_time": 5,
        "description": "바나나 우유 스무디!!",
        "process": "바나나을 껍질을 벗긴 후 얇게 슬라이스하여 얼린다. 1개 반 분량의 언 바나나를 꺼내어 우유 150ml와 함게 믹서기에 넣고 갈아준다. 거품기로 휘핑을 해준다. ",
        "cuisine_name": "스무디"
        },
        {
        "recipe_id": 8,
        "cook_time": 60,
        "description": "간단한 기본 케이크",
        "process": "계란(4개) 흰자와 노른자를 분리한 후 계란 흰자에 설탕(120g)을 넣어주면서 머랭을 만들어준다. 머랭에 노른자를 넣어 휘핑해준다. 체친 밀가루(120g)를 넣고 올리브오(30g)일을 넣어 반죽을 골고루 섞어 준다. 둥근틀에 유산지를 깔고 180도 오븐에 40분간 구워준다.",
        "cuisine_name": "케이크"
        }
    ]
    sql = "INSERT INTO api_recipe (recipe_id, cook_time, description, process, cuisine_name) VALUES (%s, %s, %s, %s, %s)"
    with connection.cursor() as cursor:
        for recipe in recipe_data:
            cursor.execute(sql, [recipe['recipe_id'], recipe['cook_time'], recipe['description'], recipe['process'], recipe['cuisine_name']])
    return

def dummy_ingredient_add():
    ingredient_data = [
        {"ingredient_name": "돼지고기", "type": "육류", "calories": 242},
        {"ingredient_name": "면", "type": "면", "calories": 250},
        {"ingredient_name": "생강", "type": "채소", "calories": 79},
        {"ingredient_name": "두반장", "type": "소스", "calories": 100},
        {"ingredient_name": "마늘", "type": "채소", "calories": 102},
        {"ingredient_name": "설탕", "type": "소스", "calories": 386},
        {"ingredient_name": "미소", "type": "소스", "calories": 198},
        {"ingredient_name": "김치", "type": "반찬", "calories": 22},
        {"ingredient_name": "대파", "type": "채소", "calories": 33},
        {"ingredient_name": "된장", "type": "소스", "calories": 199},
        {"ingredient_name": "고춧가루", "type": "소스", "calories": 281},
        {"ingredient_name": "간장", "type": "소스", "calories": 53},
        {"ingredient_name": "돼지갈비", "type": "육류", "calories": 240},
        {"ingredient_name": "소금", "type": "소스", "calories": 0},
        {"ingredient_name": "사과", "type": "과일", "calories": 52},
        {"ingredient_name": "배", "type": "과일", "calories": 57},
        {"ingredient_name": "계란", "type": "기타", "calories": 155},
        {"ingredient_name": "피자치즈", "type": "기타", "calories": 310},
        {"ingredient_name": "당근", "type": "채소", "calories": 41},
        {"ingredient_name": "양파", "type": "채소", "calories": 39},
        {"ingredient_name": "햄", "type": "육류", "calories": 145},
        {"ingredient_name": "새우", "type": "해산물", "calories": 106},
        {"ingredient_name": "애호박", "type": "채소", "calories": 16},
        {"ingredient_name": "고추장", "type": "소스", "calories": 223},
        {"ingredient_name": "참기름", "type": "소스", "calories": 884},
        {"ingredient_name": "바나나", "type": "과일", "calories": 88},
        {"ingredient_name": "우유", "type": "유제품", "calories": 42},
        {"ingredient_name": "밀가루", "type": "기타", "calories": 364},
        {"ingredient_name": "올리브오일", "type": "기타", "calories": 884},

    ]
    sql = "INSERT INTO api_ingredient (ingredient_name, type, calories) VALUES (%s, %s, %s)"
    with connection.cursor() as cursor:
        for ingredient in ingredient_data:
            cursor.execute(sql, [ingredient['ingredient_name'], ingredient['type'], ingredient['calories']])
    return

def dummy_review_add():
    review_data = [
        {"review_id": 1, "content": "맛있는 라면이에요!", "user_id": 1, "recipe_id": 1},
        {"review_id": 2, "content": "엄마가 해주시던 김치찌개 맛이 나네요..ㅠㅠ", "user_id": 2, "recipe_id": 2},
        {"review_id": 3, "content": "아이들이 너무 좋아했어요!", "user_id": 3, "recipe_id": 3},
        {"review_id": 4, "content": "조리가 너무 간단해서 좋았어요!", "user_id": 4, "recipe_id": 4},
    ]
    sql = "INSERT INTO api_review (review_id, content, user_id, recipe_id) VALUES (%s, %s, %s, %s)"
    with connection.cursor() as cursor:
        for review in review_data:
            cursor.execute(sql, [review['review_id'], review['content'], review['user_id'], review['recipe_id']])
    return

def dummy_recipe_needs_ingredient_add():
    recipe_needs_ingredient_data = [
        {"recipe_id": 1, "ingredient_name": "돼지고기"},
        {"recipe_id": 1, "ingredient_name": "면"},
        {"recipe_id": 1, "ingredient_name": "생강"},
        {"recipe_id": 1, "ingredient_name": "두반장"},
        {"recipe_id": 1, "ingredient_name": "마늘"},
        {"recipe_id": 1, "ingredient_name": "설탕"},
        {"recipe_id": 1, "ingredient_name": "미소"},

        {"recipe_id": 2, "ingredient_name": "돼지고기"},
        {"recipe_id": 2, "ingredient_name": "김치"},
        {"recipe_id": 2, "ingredient_name": "대파"},
        {"recipe_id": 2, "ingredient_name": "된장"},
        {"recipe_id": 2, "ingredient_name": "마늘"},
        {"recipe_id": 2, "ingredient_name": "고춧가루"},
        {"recipe_id": 2, "ingredient_name": "간장"},

        {"recipe_id": 3, "ingredient_name": "돼지갈비"},
        {"recipe_id": 3, "ingredient_name": "간장"},
        {"recipe_id": 3, "ingredient_name": "설탕"},
        {"recipe_id": 3, "ingredient_name": "마늘"},
        {"recipe_id": 3, "ingredient_name": "대파"},
        {"recipe_id": 3, "ingredient_name": "소금"},
        {"recipe_id": 3, "ingredient_name": "사과"},
        {"recipe_id": 3, "ingredient_name": "배"},

        {"recipe_id": 4, "ingredient_name": "계란"},
        {"recipe_id": 4, "ingredient_name": "피자치즈"},
        {"recipe_id": 4, "ingredient_name": "당근"},
        {"recipe_id": 4, "ingredient_name": "양파"},
        {"recipe_id": 4, "ingredient_name": "소금"},
        
        {"recipe_id": 5, "ingredient_name": "햄"},
        {"recipe_id": 5, "ingredient_name": "양파"},
        {"recipe_id": 5, "ingredient_name": "대파"},
        {"recipe_id": 5, "ingredient_name": "당근"},
        {"recipe_id": 5, "ingredient_name": "계란"},
        {"recipe_id": 5, "ingredient_name": "새우"},
        {"recipe_id": 5, "ingredient_name": "소금"},
        {"recipe_id": 5, "ingredient_name": "간장"},

        {"recipe_id": 6, "ingredient_name": "돼지고기"},
        {"recipe_id": 6, "ingredient_name": "애호박"},
        {"recipe_id": 6, "ingredient_name": "당근"},
        {"recipe_id": 6, "ingredient_name": "양파"},
        {"recipe_id": 6, "ingredient_name": "고추장"},
        {"recipe_id": 6, "ingredient_name": "간장"},
        {"recipe_id": 6, "ingredient_name": "설탕"},
        {"recipe_id": 6, "ingredient_name": "소금"},
        {"recipe_id": 6, "ingredient_name": "참기름"},
        
        {"recipe_id": 7, "ingredient_name": "바나나"},
        {"recipe_id": 7, "ingredient_name": "우유"},
        
        {"recipe_id": 8, "ingredient_name": "밀가루"},
        {"recipe_id": 8, "ingredient_name": "계란"},
        {"recipe_id": 8, "ingredient_name": "올리브오일"},
        {"recipe_id": 8, "ingredient_name": "설탕"},
    ]
    sql = "INSERT INTO api_recipe_needs_ingredient (recipe_id, ingredient_name) VALUES (%s, %s)"
    with connection.cursor() as cursor:
        for rni in recipe_needs_ingredient_data:
            cursor.execute(sql, [rni['recipe_id'], rni['ingredient_name']])
    return

def dummy_refrigerator_add():
    refrigerator_data = [
        {"refrigerator_id": 1, "user_id": 1, "created_at": "2021-01-01 00:00:00", "capacity": 300},
        {"refrigerator_id": 2, "user_id": 2, "created_at": "2021-01-01 00:00:00", "capacity": 300},
        {"refrigerator_id": 3, "user_id": 3, "created_at": "2021-01-01 00:00:00", "capacity": 300},
        {"refrigerator_id": 4, "user_id": 4, "created_at": "2021-01-01 00:00:00", "capacity": 300},
    ]
    sql = "INSERT INTO api_refrigerator (refrigerator_id, user_id, created_at, capacity) VALUES (%s, %s, %s, %s)"
    with connection.cursor() as cursor:
        for refrigerator in refrigerator_data:
            cursor.execute(sql, [refrigerator['refrigerator_id'], refrigerator['user_id'], refrigerator['created_at'], refrigerator['capacity']])
    return


def dummy_refrigerator_stores_ingredient_add():
    refrigerator_stores_ingredient_data = [
        {"refrigerator_id": 1, "ingredient_name": "돼지고기"},
        {"refrigerator_id": 1, "ingredient_name": "면"},
        {"refrigerator_id": 1, "ingredient_name": "생강"},
        {"refrigerator_id": 1, "ingredient_name": "두반장"},
        {"refrigerator_id": 1, "ingredient_name": "마늘"},
        {"refrigerator_id": 1, "ingredient_name": "설탕"},
        {"refrigerator_id": 1, "ingredient_name": "미소"},
        {"refrigerator_id": 1, "ingredient_name": "김치"},
        {"refrigerator_id": 1, "ingredient_name": "대파"},
        {"refrigerator_id": 1, "ingredient_name": "된장"},
        {"refrigerator_id": 1, "ingredient_name": "고춧가루"},
        {"refrigerator_id": 1, "ingredient_name": "간장"},
        {"refrigerator_id": 1, "ingredient_name": "돼지갈비"},
        {"refrigerator_id": 1, "ingredient_name": "소금"},
        {"refrigerator_id": 1, "ingredient_name": "사과"},
        {"refrigerator_id": 1, "ingredient_name": "배"},

        {"refrigerator_id": 2, "ingredient_name": "계란"},
        {"refrigerator_id": 2, "ingredient_name": "피자치즈"},
        {"refrigerator_id": 2, "ingredient_name": "당근"},
        {"refrigerator_id": 2, "ingredient_name": "양파"},
        {"refrigerator_id": 2, "ingredient_name": "소금"},
        {"refrigerator_id": 2, "ingredient_name": "햄"},
        {"refrigerator_id": 2, "ingredient_name": "대파"},
        {"refrigerator_id": 2, "ingredient_name": "새우"},
        {"refrigerator_id": 2, "ingredient_name": "간장"},
        {"refrigerator_id": 2, "ingredient_name": "돼지고기"},
        {"refrigerator_id": 2, "ingredient_name": "애호박"},
        {"refrigerator_id": 2, "ingredient_name": "고추장"},
        {"refrigerator_id": 2, "ingredient_name": "설탕"},
        {"refrigerator_id": 2, "ingredient_name": "참기름"},


        {"refrigerator_id": 3, "ingredient_name": "바나나"},
        {"refrigerator_id": 3, "ingredient_name": "우유"},
        {"refrigerator_id": 3, "ingredient_name": "밀가루"},
        {"refrigerator_id": 3, "ingredient_name": "계란"},
        {"refrigerator_id": 3, "ingredient_name": "올리브오일"},
        {"refrigerator_id": 3, "ingredient_name": "설탕"},
    ]
    sql = "INSERT INTO api_refrigerator_stores_ingredient (refrigerator_id, ingredient_name) VALUES (%s, %s)"
    with connection.cursor() as cursor:
        for rsi in refrigerator_stores_ingredient_data:
            cursor.execute(sql, [rsi['refrigerator_id'], rsi['ingredient_name']])
    return
