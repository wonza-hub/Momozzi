import { useSelector } from "react-redux";
import axios from "axios";
import { useQueryClient, useMutation } from "@tanstack/react-query";

/**
 * 리뷰 단건
 * @param { object, boolean }
 * @returns
 */
const ReviewListItem = ({ review, isReadingReviews }) => {
  const user = useSelector((state) => state.user);

  const { mutate: deleteReview, isPending } = useDeleteReview();

  const handleReviewDeletion = () => {
    deleteReview(review.review_id);
  };

  return (
    <>
      {isReadingReviews || isPending ? null : (
        <div
          className="relative w-full mb-4 py-4 px-6 bg-white rounded-3xl shadow-[0px_10px_1px_rgba(221,_221,_221,_1),_0_10px_20px_rgba(204,_204,_204,_1)]"
          key={review.review_id}
        >
          <div className="mb-4 pr-16 text-xl text-black/90">
            {review.content}
          </div>
          <div className="text-md text-black/90 text-right pr-4">
            {review.last_name}
          </div>
          {review.user_id === user.id ? (
            <button
              className="absolute right-5 top-3 p-1 text-sm"
              onClick={handleReviewDeletion}
            >
              삭제
            </button>
          ) : null}
        </div>
      )}
    </>
  );
};

// REST: 단건 리뷰 삭제
const useDeleteReview = () => {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: async (targetReviewId) => {
      const reviewDelURL = `${process.env.REACT_APP_SERVER}/api/review/`;
      return await axios.delete(reviewDelURL, {
        data: {
          review_id: targetReviewId,
        },
      });
    },
    onSuccess: () => {
      queryClient.invalidateQueries(["recipe-reviews"]);
    },
  });
};

export default ReviewListItem;
