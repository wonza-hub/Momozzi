/**
 * 레시피 추천 버튼 컴포넌트
 * @param {method, category} param0
 * @returns
 */
const RecommendBtn = ({ method, onRecommendClick }) => {
  return (
    <>
      <button
        className="w-44 h-12 mt-3 px-4 float-right bg-primary/90 text-xl text-white rounded-xl hover:bg-primary duration-300"
        onClick={onRecommendClick}
      >
        Recommend!
      </button>
    </>
  );
};

export default RecommendBtn;
