import { useState, useEffect } from "react";
import { useSelector } from "react-redux";
import axios from "axios";
import { Link } from "react-router-dom";

/**
 * 프로필 페이지
 * @returns
 */
const Mypage = () => {
  const [favoriteCuisines, setFavoriteCuisines] = useState([]);
  const [myRefrigerators, setMyRefrigerators] = useState([]);
  const user = useSelector((state) => state.user);

  useEffect(() => {
    // GET: 사용자 보유 냉장고 조회
    let openFridgeURL = `${process.env.REACT_APP_SERVER}/api/refrigerator/?user_id=${user.id}`;
    axios?.get(openFridgeURL)?.then((res) => {
      setMyRefrigerators(res.data);
    });
  }, [user.id]);

  useEffect(() => {
    // GET: 사용자 선호 요리 조회
    let favoriteCuisineURL = `${process.env.REACT_APP_SERVER}/api/user_likes_cuisine/?user_id=${user.id}`;
    axios?.get(favoriteCuisineURL)?.then((res) => {
      // console.log(res.data);
      setFavoriteCuisines(res.data);
    });
  }, [user.id]);

  return (
    <>
      <div className="relative min-w-screen min-h-screen bg-[#DBDBDB]/20">
        {/* box shadows - next.js */}
        <div className="absolute w-[480px] min-h-[620px] bg-white/80 top-[450px] left-2/4 -translate-x-2/4 -translate-y-[320px] px-12 pt-10 rounded-2xl opacity-85 shadow-[0_8px_30px_rgb(0,0,0,0.12)]">
          <header className="mb-4 text-xl font-bold text-primary drop-shadow-sm">
            이름
          </header>
          <div className="font-semibold text-lg text-black">{user.name}</div>
          <header className="my-4 text-xl font-bold text-primary drop-shadow-sm">
            좋아하는 요리
          </header>
          <div className="flex flex-row">
            {favoriteCuisines.map((cuisine) => (
              <div className="mr-2 px-2 py-1 bg-slate-200 rounded-xl border-2 border-secondary">
                {cuisine.cuisine_name}
              </div>
            ))}
          </div>
          <header className="my-4 text-xl font-bold text-primary drop-shadow-sm">
            나의 냉장고
          </header>
          <div className="w-full mb-2 flex flex-row">
            <span className="mx-8">용량</span>
            <span className="mx-10">생성일자</span>
          </div>
          {myRefrigerators.map((refrigerator) => (
            <div className="w-full py-2 bg-slate-200 rounded-xl border-2 border-secondary flex flex-row">
              <span className="mr-8 pl-8 text-black">
                {refrigerator.capacity}
              </span>
              <span className="mr-8 text-black">{refrigerator.created_at}</span>
              <Link
                to={`../refrigerator/${refrigerator.refrigerator_id}`}
                key={refrigerator.refrigerator_id}
              >
                <span className="mx-6">열기</span>
              </Link>
            </div>
          ))}
        </div>
      </div>
    </>
  );
};

export default Mypage;
