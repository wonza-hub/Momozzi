import Inventory from "./Inventory";
import DropDown from "../../components/DropDown";
import OpenBtn from "./OpenBtn";
import RecommendBtn from "./RecommendBtn";
import { METHOD, CATEGORY } from "../../constants/Constant";
import { useState } from "react";
import axios from "axios";

const Refrigerator = () => {
  const [method, setMethod] = useState("");
  const [category, setCategory] = useState("");
  const [storedIngredients, setStoredIngredients] = useState([]);

  return (
    <>
      {/* <Inventory storedIngredients={storedIngredients}></Inventory> */}
      <div>
        <div>
          <span>Method</span>
          <DropDown menuItems={METHOD} setArg={setMethod}></DropDown>
        </div>
        <div>
          <span>Category</span>
          <DropDown menuItems={CATEGORY} setArg={setCategory}></DropDown>
        </div>
      </div>
      <RecommendBtn method={method} category={category}></RecommendBtn>
      <OpenBtn
        // userId={userId}
        setStoredIngredients={setStoredIngredients}
      ></OpenBtn>
    </>
  );
};

export default Refrigerator;
