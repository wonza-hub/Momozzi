import { useNavigate } from "react-router-dom";

const RecommendBtn = ({ method, category, userId }) => {
  const navigate = useNavigate();

  return (
    <>
      <button
        className="w-44 h-12 px-4 my-auto bg-primary/90 text-xl text-white rounded-xl hover:bg-primary duration-300"
        onClick={() => {
          if (method || category) {
            navigate("/recommend", {
              state: {
                foodFilter: {
                  method,
                  category,
                },
              },
            });
          } else {
            alert("요리 방법이나 카테고리를 입력해주세요.");
          }
        }}
      >
        Recommend!
      </button>
    </>
  );
};

export default RecommendBtn;
