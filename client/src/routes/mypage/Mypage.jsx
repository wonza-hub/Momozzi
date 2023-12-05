import { useState, useEffect } from "react";
import { useSelector } from "react-redux";
import axios from "axios";
import { Link } from "react-router-dom";

const Mypage = () => {
  const [favoriteCuisines, setFavoriteCuisines] = useState([]);
  const [myRefrigerators, setMyRefrigerators] = useState([]);
  const user = useSelector((state) => state.user);

  useEffect(() => {
    // 사용자 보유 냉장고 조회
    let openFridgeUrl = `${process.env.REACT_APP_SERVER}/api/refrigerator/?user_id=${user.id}`;
    axios?.get(openFridgeUrl)?.then((res) => {
      console.log(res.data);
      setMyRefrigerators(res.data);
    });
  }, [user.id]);

  return (
    <>
      <div className="relative min-w-screen min-h-screen bg-[#DBDBDB]/20">
        {/* box shadows - next.js */}
        <div className="absolute w-[480px] min-h-[620px] bg-white/80 top-[450px] left-2/4 -translate-x-2/4 -translate-y-[320px] px-12 pt-10 rounded-2xl opacity-85 shadow-[0_8px_30px_rgb(0,0,0,0.12)]">
          <header className="mb-5 text-xl font-bold text-primary drop-shadow-sm">
            이름
          </header>
          {/* {user.} */}
          <header className="mb-5 text-xl font-bold text-primary drop-shadow-sm">
            좋아하는 요리
          </header>
          <div>
            <ul>
              {/* {favoriteCuisines.map(() => (
                <li></li>
              ))} */}
            </ul>
          </div>
          <header className="mb-5 text-xl font-bold text-primary drop-shadow-sm">
            나의 냉장고
          </header>
          <div className="w-full mb-2 flex flex-row justify-around">
            <span>용량</span>
            <span>생성일자</span>
          </div>
          {myRefrigerators.map((refrigerator) => (
            <Link to={`../refrigerator/${refrigerator.refrigerator_id}`}>
              <div className="w-full bg-slate-200 rounded-xl border-2 border-secondary flex flex-row justify-around">
                <span className="">{refrigerator.capacity}</span>
                <span>{refrigerator.created_at}</span>
              </div>
            </Link>
          ))}
        </div>
      </div>
    </>
  );
};

export default Mypage;
