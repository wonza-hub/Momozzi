import { useSelector } from "react-redux";
import axios from "axios";

/**
 *
 * @param {review, onDeleteReview} onDeleteReview:리뷰삭제 콜백함수
 * @returns
 */
const Review = ({ review, onDeleteReview }) => {
  const user = useSelector((state) => state.user);

  const deleteReview = () => {
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
      })
      .catch(() => console.log("delete fail"));
  };

  return (
    <>
      <div
        className="relative w-full mb-4 py-3 px-5 bg-white rounded-3xl shadow-[0px_10px_1px_rgba(221,_221,_221,_1),_0_10px_20px_rgba(204,_204,_204,_1)]"
        key={review.review_id}
      >
        <div className="text-xl text-black/90">{review.content}</div>
        <div className="text-md text-black/90 text-right pr-4">
          {review.username}
        </div>
        {review.user_id === user.id ? (
          <button
            className="absolute right-3 bottom-1 p-1 text-md"
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
