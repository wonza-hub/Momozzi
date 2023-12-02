import { createSlice } from "@reduxjs/toolkit";

export const userReducer = createSlice({
  name: "user",
  initialState: {
    name: "",
    id: "",
    isLoading: false,
    isLogin: null,
  },
  reducers: {
    loginUser: (state, action) => {
      state.id = action.payload.user_id;
      state.name = action.payload.last_name;
      state.isLogin = true;
    },

    clearUser: (state) => {
      state.name = "";
      state.id = "";
      state.isLogin = false;
    },
  },
});

export const { loginUser, clearUser } = userReducer.actions;
export default userReducer;
