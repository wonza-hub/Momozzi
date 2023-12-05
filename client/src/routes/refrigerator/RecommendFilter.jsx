import { METHOD, CATEGORY } from "../../constants/Constant";
import DropDown from "../../components/DropDown";

/**
 * 레시피 추천 필터 컴포넌트
 * @returns
 */
const RecommendFilter = ({ setMethod, setCategory }) => {
  return (
    <>
      <div className="flex flex-row justify-evenly mt-8 mb-12">
        <div>
          <div className="flex flex-row justify-between w-80 mb-4">
            <span className="text-xl font-semibold text-primary/90">
              Method
            </span>
            <DropDown menuItems={METHOD} setArg={setMethod}></DropDown>
          </div>
          <div className="flex flex-row w-80 justify-between">
            <span className="text-xl font-semibold text-primary/90">
              Category
            </span>
            <DropDown menuItems={CATEGORY} setArg={setCategory}></DropDown>
          </div>
        </div>
      </div>
    </>
  );
};

export default RecommendFilter;
