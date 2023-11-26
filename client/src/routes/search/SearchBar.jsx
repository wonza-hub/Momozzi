import {
  Radio,
  RadioGroup,
  FormControlLabel,
  FormControl,
} from "@mui/material";
import { useState } from "react";
import { METHOD, CATEGORY, INGREDIENT } from "../../constants/Constant.js";
import axios from "axios";

const SearchBar = () => {
  const [method, setMethod] = useState("");
  const [category, setCategory] = useState("");
  const [ingredient, setIngredients] = useState("");
  console.log(method);
  console.log(category);
  console.log(ingredient);

  const handleMethodChange = (event) => {
    setMethod(event.target.value);
  };
  const handleCategoryChange = (event) => {
    setCategory(event.target.value);
  };
  const handleIngredientsChange = (event) => {
    setIngredients(event.target.value);
  };

  return (
    <>
      <div className="w-[336px] px-[25px] pt-[100px] h-screen max-h-screen bg-secondary/80">
        <FormControl>
          <header className="mb-2 text-[24px] font-semibold text-primary/90">
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
        </FormControl>
      </div>
    </>
  );
};

export default SearchBar;
