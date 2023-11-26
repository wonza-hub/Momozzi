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
      <div className="absolute left-2/4 bg-[url('./img/fridge_bg.png')] w-2/4 h-screen"></div>
      <div className="relative min-w-screen min-h-screen bg-[#DBDBDB]/20">
        {/* box shadows - next.js */}
        <div className="absolute bg-white/80 top-[450px] left-2/4 min-h-[560px] -translate-x-2/4 -translate-y-[320px] px-12 pt-10 rounded-2xl opacity-85 shadow-[0_8px_30px_rgb(0,0,0,0.12)]">
          <Inventory storedIngredients={storedIngredients}></Inventory>
          <div className="flex flex-row justify-evenly mt-8 mb-12">
            <div>
              <div className="flex flex-row justify-between w-80 mb-4">
                <span className="text-xl font-semibold text-primary/90">
                  Method
                </span>
                <DropDown menuItems={METHOD} setArg={setMethod}></DropDown>
              </div>
              <div className="flex flex-row w-80 justify-between">
                <span className="text-xl font-semibold text-primary/90">
                  Category
                </span>
                <DropDown menuItems={CATEGORY} setArg={setCategory}></DropDown>
              </div>
            </div>
            <RecommendBtn method={method} category={category}></RecommendBtn>
          </div>
        </div>
        <OpenBtn
          // userId={userId}
          setStoredIngredients={setStoredIngredients}
        ></OpenBtn>
      </div>
    </>
  );
};

export default Refrigerator;
