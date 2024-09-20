import { createStore } from "vuex";
import axios from "axios";

export default createStore({
  state: {
    words: [],
    teacherGroups: [],
    studentGroups: [],
    student: null,
    teacher: null,
    group: null,
    isAuthenticated: false,
    token: "",
    isLoading: false,
  },
  getters: {
    getWordById: (state) => (wordId) => {
      return state.words.find((word) => word.id === wordId);
    },
    unlearnedWords(state) {
      return state.words.filter((word) => word.is_learned === false);
    },
  },
  mutations: {
    initializeStore(state) {
      if (localStorage.getItem("token")) {
        state.token = localStorage.getItem("token");
        state.isAuthenticated = true;
      } else {
        state.token = "";
        state.isAuthenticated = false;
      }
    },
    setIsLoading(state, status) {
      state.isLoading = status;
    },
    setToken(state, token) {
      state.token = token;
      state.isAuthenticated = true;
    },
    removeToken(state) {
      state.token = "";
      state.isAuthenticated = false;
    },
    setWords(state, words) {
      state.words = words;
    },
    setTeacherGroups(state, groups) {
      state.teacherGroups = groups;
    },
    setStudentGroups(state, groups) {
      state.studentGroups = groups;
    },
    setGroup(state, group) {
      state.group = group;
    },
    setStudent(state, student) {
      state.student = student;
    },
    setTeacher(state, teacher) {
      state.teacher = teacher;
    },
    addWord(state, word) {
      state.words.push(word);
    },
    addGroup(state, group) {
      state.teacherGroups.push(group);
    },
    addToGroup(state, group) {
      state.studentGroups.push(group);
    },
    deleteWord(state, wordId) {
      state.words = state.words.filter((word) => word.id !== wordId);
    },
    deleteGroup(state, groupID) {
      state.teacherGroups = state.teacherGroups.filter((group) => group.group_id !== groupID);
    },
    updateWord(state, updatedWord) {
      const index = state.words.findIndex(word => word.id === updatedWord.id);
      if (index !== -1) {
        state.words.splice(index, 1, updatedWord);
      }
    },
    updateWordStatus(state, updatedWord) {
      const index = state.words.findIndex(word => word.id === updatedWord.id);
      if (index !== -1) {
        state.words.splice(index, 1, updatedWord);
      }
    },
  },
  actions: {
    async fetchWords({ commit }) {
      try {
        const token = localStorage.getItem("token");
        const config = {
          headers: { Authorization: `Bearer ${token}` },
        };
        const response = await axios.get("/api/v1/vocab/", config);
        if (response.data.data != null) {
        response.data.data.sort((a, b) => {
          return b.created_at.seconds - a.created_at.seconds;
        });}
        commit("setWords", response.data.data);
      } catch (error) {
        console.error(error);
      }
    },
    async fetchStats({ commit }, formData) {
      try {
        const token = localStorage.getItem("token");
        const config = {
          headers: { Authorization: `Bearer ${token}` },
        };
        const response = await axios.post("/api/v1/group/get_statistics", formData, config);
        response.data.data.words.sort((a, b) => {
          return b.created_at.seconds - a.created_at.seconds;
        });        
        return response.data.data;
      } catch (error) {
        console.error(error);
      }
    },
    async fetchTeacherGroups({ commit }) {
      try {
        const token = localStorage.getItem("token");
        const config = {
          headers: { Authorization: `Bearer ${token}` },
        };
        const response = await axios.get("/api/v1/group/find_teacher/", config);    
        commit("setTeacherGroups", response.data.data);
      } catch (error) {
        console.error(error);
      }
    },
    async fetchStudentGroups({ commit }) {
      try {
        const token = localStorage.getItem("token");
        const config = {
          headers: { Authorization: `Bearer ${token}` },
        };
        const response = await axios.get("/api/v1/group/find_student/", config);    
        commit("setStudentGroups", response.data.data);
      } catch (error) {
        console.error(error);
      }
    },
    async fetchGroup({ commit }, formData) {
      try {
        const token = localStorage.getItem("token");
        const config = {
          headers: { Authorization: `Bearer ${token}` },
        };
        const response = await axios.post("/api/v1/group/find/", formData, config);    
        commit("setGroup", response.data.data);
      } catch (error) {
        console.error(error);
      }
    },
    async findStudent({ commit }, formData) {
      try {
        const token = localStorage.getItem("token");
        const config = {
          headers: { Authorization: `Bearer ${token}` },
        };
        const response = await axios.post("/api/v1/group/find_student_info/", formData, config);    
        commit("setStudent", response.data.data);
        return response.data.data
      } catch (error) {
        console.error(error);
      }
    },
    async findTeacher({ commit }, formData) {
      try {
        const token = localStorage.getItem("token");
        const config = {
          headers: { Authorization: `Bearer ${token}` },
        };
        const response = await axios.post("/api/v1/group/find_teacher_info/", formData, config);    
        commit("setTeacher", response.data.data);
        return response.data.data
      } catch (error) {
        console.error(error);
      }
    },
    async addWord({ commit }, formData) {
      try {
        const token = localStorage.getItem("token");
        const config = {
          headers: { Authorization: `Bearer ${token}` },
        };
        const response = await axios.post("/api/v1/vocab/", formData, config);
        const newWord = response.data;
        commit("addWord", newWord);
      } catch (error) {
        console.error(error);
      }
    },
    async addWordToStudent({ commit }, formData) {
      try {
        const token = localStorage.getItem("token");
        const config = {
          headers: { Authorization: `Bearer ${token}` },
        };
        await axios.post("/api/v1/group/add_word/", formData, config);
      } catch (error) {
        console.error(error);
      }
    },
    async addGroup({ commit }, formData) {
      try {
        const token = localStorage.getItem("token");
        const config = {
          headers: { Authorization: `Bearer ${token}` },
        };
        const response = await axios.post("/api/v1/group/", formData, config);
        const newGroup = response.data;
        commit("addGroup", newGroup);
      } catch (error) {
        console.error(error);
      }
    },
    async addToGroup({ commit }, formData) {
      try {
        const token = localStorage.getItem("token");
        const config = {
          headers: { Authorization: `Bearer ${token}` },
        };
        const response = await axios.post("/api/v1/group/add/", formData, config);
        const newGroup = response.data;
        commit("addToGroup", newGroup);
      } catch (error) {
        console.error(error);
      }
    },
    async deleteWord({ commit }, wordId) {
      try {
        const token = localStorage.getItem("token");
        const config = {
          headers: { Authorization: `Bearer ${token}` },
        };
        await axios.delete(`/api/v1/vocab/${wordId}`, config);
        commit("deleteWord", wordId);
      } catch (error) {
        console.error(error);
      }
    },
    async deleteGroup({ commit }, groupId) {
      try {
        const token = localStorage.getItem("token");
        const config = {
          headers: { Authorization: `Bearer ${token}` },
        };
        await axios.delete(`/api/v1/group/${groupId}`, config);
        commit("deleteGroup", groupId);
      } catch (error) {
        console.error(error);
      }
    },
    async updateWord({ commit }, formData) {
      try {
        const token = localStorage.getItem("token");
        const config = {
          headers: { Authorization: `Bearer ${token}` },
        };
        const response = await axios.patch(`/api/v1/vocab/${formData.id}`, formData, config);
        const updatedWord = response.data;
        commit("updateWord", updatedWord);
      } catch (error) {
        console.error(error);
      }
    },
    async updateWordStatus({ commit }, formData) {
      try {
        const token = localStorage.getItem("token");
        const config = {
          headers: { Authorization: `Bearer ${token}` },
        };
        const response = await axios.patch(`/api/v1/vocab/${formData.id}/status`, formData, config);
        const updatedWordStatus = response.data;
        commit("updateWordStatus", updatedWordStatus);
      } catch (error) {
        console.error(error);
      }
    },
  },
  modules: {},
});
