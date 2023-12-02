import Inventory from "./Inventory";
import IngredientRegistration from "./IngredientRegistration";
import RecommendFilter from "./RecommendFilter";
import { useState, useEffect } from "react";
import { useSelector } from "react-redux";
import axios from "axios";

const Refrigerator = () => {
  const [storedIngredients, setStoredIngredients] = useState([]);
  const user = useSelector((state) => state.user);

  useEffect(() => {
    let openFridgeUrl = `${process.env.REACT_APP_SERVER}/api/refrigerator/?user_id=1`;
    axios?.get(openFridgeUrl)?.then((res) => {
      console.log(res);
      setStoredIngredients(res.data);
    });
  }, []);

  return (
    <>
      <div className="absolute left-2/4 bg-[url('./img/fridge_bg.png')] w-2/4 h-screen"></div>
      <div className="relative min-w-screen min-h-screen bg-[#DBDBDB]/20">
        {/* box shadows - next.js */}
        <div className="absolute bg-white/80 top-[450px] left-2/4 min-h-[560px] -translate-x-2/4 -translate-y-[320px] px-12 pt-10 rounded-2xl opacity-85 shadow-[0_8px_30px_rgb(0,0,0,0.12)]">
          <Inventory storedIngredients={storedIngredients}></Inventory>
          <IngredientRegistration
            setStoredIngredients={setStoredIngredients}
          ></IngredientRegistration>
          <RecommendFilter></RecommendFilter>
        </div>
      </div>
    </>
  );
};

export default Refrigerator;
