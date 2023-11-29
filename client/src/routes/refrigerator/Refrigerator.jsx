import Inventory from "./Inventory";
import OpenBtn from "./OpenBtn";
import RecommendFilter from "./RecommendFilter";
import { useState } from "react";
import axios from "axios";

const Refrigerator = () => {
  const [storedIngredients, setStoredIngredients] = useState([]);

  return (
    <>
      <div className="absolute left-2/4 bg-[url('./img/fridge_bg.png')] w-2/4 h-screen"></div>
      <div className="relative min-w-screen min-h-screen bg-[#DBDBDB]/20">
        {/* box shadows - next.js */}
        <div className="absolute bg-white/80 top-[450px] left-2/4 min-h-[560px] -translate-x-2/4 -translate-y-[320px] px-12 pt-10 rounded-2xl opacity-85 shadow-[0_8px_30px_rgb(0,0,0,0.12)]">
          <Inventory storedIngredients={storedIngredients}></Inventory>
          <RecommendFilter></RecommendFilter>
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
