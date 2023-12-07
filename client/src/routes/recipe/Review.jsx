import { useSelector } from "react-redux";
import axios from "axios";

/**
 * 리뷰 단건 컴포넌트
 * @param {review, onDeleteReview} onDeleteReview:리뷰삭제 콜백함수
 * @returns
 */
const Review = ({ review, onDeleteReview }) => {
  const user = useSelector((state) => state.user);

  const deleteReview = () => {
    // DELETE: 단건 리뷰 삭제
    const reviewDelURL = `${process.env.REACT_APP_SERVER}/api/review/`;
    axios
      .delete(reviewDelURL, {
        data: {
          review_id: review.review_id,
        },
      })
      .then((res) => {
        if (res.status === 200) {
          onDeleteReview(review.review_id);
        }
      });
  };

  return (
    <>
      <div
        className="relative w-full mb-4 py-4 px-6 bg-white rounded-3xl shadow-[0px_10px_1px_rgba(221,_221,_221,_1),_0_10px_20px_rgba(204,_204,_204,_1)]"
        key={review.review_id}
      >
        <div className="mb-4 text-xl text-black/90">{review.content}</div>
        <div className="text-md text-black/90 text-right pr-4">
          {review.last_name}
        </div>
        {review.user_id === user.id ? (
          <button
            className="absolute right-5 top-2 p-1 text-sm"
            onClick={deleteReview}
          >
            삭제
          </button>
        ) : null}
      </div>
    </>
  );
};

export default Review;
