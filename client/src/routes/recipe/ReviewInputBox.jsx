import { useState, useRef } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";

const ReviewInputBox = ({ setReviews }) => {
  const { reviewPostId } = useParams();

  const [isLoading, setIsLoading] = useState(false);
  const [newReview, setNewReview] = useState("");

  const reviewInputRef = useRef(null);

  const handleReviewInputChange = () => {
    setNewReview(reviewInputRef.current.value);
  };

  const handleReviewSubmit = () => {
    const reviewPostURL = `${process.env.REACT_APP_SERVER}/review/${reviewPostId}`;
    axios
      ?.post(
        reviewPostURL,
        { newReview },
        {
          headers: {
            "Content-Type": "application/json",
          },
        }
      )
      ?.then((res) => {
        if (res.status === 200) {
          // POST 요청이 성공적으로 완료될 때, 데이터를 다시 가져와 주입
          axios
            .get(`${process.env.REACT_APP_SERVER}/`)
            .then((response) => {
              const newData = response.data;
              setReviews(newData);
              setIsLoading(false);
            })
            .catch((error) => {
              console.error("데이터를 다시 가져오는 중 오류 발생:", error);
            });
        }
      })
      ?.catch(() => console.log("post fail"));
  };

  return (
    <>
      <form className="flex-auto mr-2" onSubmit={handleReviewSubmit}>
        {isLoading ? (
          <div class="w-full h-full pt-2 pb-1 flex justify-center">
            {/* <LoadingSpinner></LoadingSpinner> */}
          </div>
        ) : (
          <input
            onChange={handleReviewInputChange}
            value={newReview}
            className="w-full h-full py-0 pl-10 pr-24 bg-[#efefef] border-none rounded-3xl outline-2 outline-primary text-xl text-black/90"
            type="text"
            placeholder="리뷰 추가"
            ref={reviewInputRef}
          />
        )}
      </form>
    </>
  );
};

export default ReviewInputBox;
