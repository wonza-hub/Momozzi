import { createSlice } from "@reduxjs/toolkit";

const loadUserFromLocalStorage = () => {
  try {
    const user = localStorage.getItem("user");
    return user ? JSON.parse(user) : null;
  } catch (error) {
    console.error("Error loading user from localStorage:", error);
    return null;
  }
};

export const userReducer = createSlice({
  name: "user",
  initialState: {
    name: "",
    id: 0,
    isLoading: false,
    isLogin: null,
  },
  reducers: {
    loginUser: (state, action) => {
      state.first_name = action.payload[0].first_name;
      state.last_name = action.payload[0].last_name;
      state.id = action.payload[0].user_id;
      state.name = state.first_name + state.last_name;
      state.isLogin = true;

      // Local Storage에 로그인정보 저장
      localStorage.setItem("user", JSON.stringify(action.payload[0]));
    },

    clearUser: (state) => {
      state.name = "";
      state.id = "";
      state.isLogin = false;

      // Local Storage의 로그인정보 삭제
      localStorage.removeItem("user");
    },

    loadUser: (state) => {
      const user = loadUserFromLocalStorage();
      if (user) {
        state.first_name = user.first_name;
        state.last_name = user.last_name;
        state.id = user.user_id;
        state.name = user.first_name + user.last_name;
        state.isLogin = true;
      }
    },
  },
});

export const { loginUser, clearUser, loadUser } = userReducer.actions;
export default userReducer;
