import { useNavigate } from "react-router-dom";

const RecommendBtn = ({ method, category, userId }) => {
  const navigate = useNavigate();

  return (
    <>
      <button
        onClick={() => {
          if (method || category) {
            navigate("/foodList", {
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