import { Radio, RadioGroup, FormControlLabel } from "@mui/material";
import { useState, useRef } from "react";
import { METHOD, CATEGORY, INGREDIENT } from "../../constants/Constant.js";
import SearchBtn from "./SearchBtn.jsx";
import SearchBox from "./SearchBox.jsx";
import axios from "axios";

const SearchBar = ({ setRecipes }) => {
  const [method, setMethod] = useState("");
  const [category, setCategory] = useState("");
  const [ingredient, setIngredients] = useState("");
  const [searchContent, setSearchContent] = useState("");
  const searchInputRef = useRef(null);

  const handleMethodChange = (event) => {
    setMethod(event.target.value);
  };
  const handleCategoryChange = (event) => {
    setCategory(event.target.value);
  };
  const handleIngredientsChange = (event) => {
    setIngredients(event.target.value);
  };

  // 검색 버튼 클릭시 데이터 요청
  const handleSearchClick = () => {
    if (method || category || ingredient) {
      const filterUrl = `${process.env.REACT_APP_SERVER}/`;
      const queryParams = {
        method: method,
        category: category,
        ingredient: ingredient,
      };
      axios
        ?.get(filterUrl, { params: queryParams })
        ?.then((res) => {
          setRecipes(res.data);
        })
        .catch((error) => {
          console.error("음식 정보 불러오기 실패", error);
        });
    } else {
      alert("필터 조건을 선택하세요");
    }
  };

  const onSearchContentChange = () => {
    const searchInputValue = searchInputRef.current.value;
    setSearchContent(searchInputValue);
  };

  // 검색창 부분 문자열 입력시 api 요청
  const handleSearchBoxInputComplete = () => {
    if (searchContent) {
      const filterUrl = `${process.env.REACT_APP_SERVER}/api/recipe/search/?keyword=${searchContent}`;
      const queryParams = {
        searchContent: searchContent,
      };
      axios
        ?.get(filterUrl, { params: queryParams })
        ?.then((res) => {
          setRecipes(res.data);
        })
        .catch((error) => {
          console.error("음식 정보 불러오기 실패", error);
        });
    } else {
      alert("검색어를 입력하세요");
    }
  };

  return (
    <>
      <div className="w-[334px] px-[28px] pt-[110px] h-screen max-h-screen bg-secondary/40">
        <header className="my-2 text-[24px] font-semibold text-primary/90">
          Method
        </header>
        <RadioGroup
          className="mb-4 h-[168px]"
          value={method}
          onChange={handleMethodChange}
        >
          {METHOD.map((method, idx) => (
            <FormControlLabel
              key={idx}
              value={method}
              control={<Radio color="success" />}
              label={method}
            />
          ))}
        </RadioGroup>
        <header className="mb-2 text-[24px] font-semibold text-primary/90">
          Category
        </header>
        <RadioGroup
          className="mb-2 h-[128px]"
          value={category}
          onChange={handleCategoryChange}
        >
          {CATEGORY.map((category, idx) => (
            <FormControlLabel
              key={idx}
              value={category}
              control={<Radio color="success" />}
              label={category}
            />
          ))}
        </RadioGroup>
        <header className="mb-2 text-[24px] font-semibold text-primary/90">
          Ingredient
        </header>
        <RadioGroup
          className="mb-2 h-[128px]"
          value={ingredient}
          onChange={handleIngredientsChange}
        >
          {INGREDIENT.map((ingredient, idx) => (
            <FormControlLabel
              key={idx}
              value={ingredient}
              control={<Radio color="success" />}
              label={ingredient}
            />
          ))}
        </RadioGroup>
        <SearchBtn handleSearchClick={handleSearchClick}></SearchBtn>
        <SearchBox
          searchContent={searchContent}
          onSearchContentChange={onSearchContentChange}
          ref={searchInputRef}
          handleSearchBoxInputComplete={handleSearchBoxInputComplete}
        ></SearchBox>
      </div>
    </>
  );
};

export default SearchBar;
