<template>
  <section
    id="sidebar"
    class="leftsidebarinner-sidebar"
    v-bind:class="rootClassName"
  >
    <div class="leftsidebarinner-sidebarheader">
      <div class="leftsidebarinner-container">
        <router-link
          :to="`/profile/${this.$store.getters.currentUser}`"
          class="leftsidebarinner-navlink button"
        >
          <span id="user.name" class="leftsidebarinner-text">{{ userFirstName }}</span>
          <span id="user.username" class="leftsidebarinner-text01">{{ userUsername }}</span>
        </router-link>
      </div>
    </div>
    <div class="leftsidebarinner-container1">
      <nav class="leftsidebarinner-nav">
        <div class="leftsidebarinner-container2">
          <router-link
            :to="`/dashboard/${this.$store.state.user.id}`"
            class="leftsidebarinner-navlink1 button"
          >
            <svg viewBox="0 0 1024 1024" class="leftsidebarinner-icon">
              <path
                d="M512 128c0 0-263.936 227.84-411.435 351.232-8.661 7.851-15.232 19.285-15.232 32.768 0 23.595 19.072 42.667 42.667 42.667h85.333v298.667c0 23.595 19.072 42.667 42.667 42.667h128c23.595 0 42.667-19.115 42.667-42.667v-170.667h170.667v170.667c0 23.552 19.072 42.667 42.667 42.667h128c23.595 0 42.667-19.072 42.667-42.667v-298.667h85.333c23.595 0 42.667-19.072 42.667-42.667 0-13.483-6.571-24.917-16.341-32.768-146.475-123.392-410.325-351.232-410.325-351.232z"
              ></path>
            </svg>
            <span class="leftsidebarinner-text02">{{ text2 }}</span>
          </router-link>
        </div>
        <div class="leftsidebarinner-container3">
          <router-link
            :to="`/messages/${this.$store.state.user.id}`"
            class="leftsidebarinner-navlink2 button"
          >
            <svg viewBox="0 0 1024 1024" class="leftsidebarinner-icon02">
              <path
                d="M896 298.667h-128c0-70.4-57.6-128-128-128h-512c-70.4 0-128 57.6-128 128v298.667c0 70.4 57.6 128 128 128v128l128-128c0 70.4 57.6 128 128 128h341.333l128 128v-128h42.667c70.4 0 128-57.6 128-128v-298.667c0-70.4-57.6-128-128-128zM128 640c-23.125 0-42.667-19.541-42.667-42.667v-298.667c0-23.125 19.541-42.667 42.667-42.667h512c23.125 0 42.667 19.541 42.667 42.667v42.667h-277.333c-58.837 0-106.667 47.829-106.667 106.667v192h-170.667zM938.667 725.333c0 23.125-19.541 42.667-42.667 42.667h-512c-23.125 0-42.667-19.541-42.667-42.667v-277.333c0-35.285 28.715-64 64-64h490.667c23.125 0 42.667 19.541 42.667 42.667v298.667z"
              ></path>
            </svg>
            <span class="leftsidebarinner-text03">Messages</span>
          </router-link>
        </div>
        <div class="leftsidebarinner-container4">
          <router-link
            :to="`/teams/${this.$store.state.user.id}`"
            class="leftsidebarinner-navlink3 button"
          >
            <svg viewBox="0 0 1024 1024" class="leftsidebarinner-icon04">
              <path
                d="M512 597.333c117.931 0 213.333-95.488 213.333-213.333s-95.403-213.333-213.333-213.333-213.333 95.488-213.333 213.333 95.403 213.333 213.333 213.333zM512 256c70.571 0 128 57.429 128 128s-57.429 128-128 128-128-57.429-128-128 57.429-128 128-128z"
              ></path>
              <path
                d="M853.333 640c58.923 0 106.667-47.659 106.667-106.667 0-58.923-47.744-106.667-106.667-106.667-58.965 0-106.667 47.744-106.667 106.667 0 59.008 47.701 106.667 106.667 106.667zM853.333 469.333c35.285 0 64 28.715 64 64s-28.715 64-64 64-64-28.715-64-64 28.715-64 64-64z"
              ></path>
              <path
                d="M853.333 665.173c-56.789 0-99.499 17.323-124.459 41.344-47.573-39.168-122.795-66.517-216.875-66.517-96.683 0-170.453 27.648-217.259 66.731-25.429-24.107-68.608-41.6-124.075-41.6-93.355 0-149.333 46.549-149.333 93.141 0 23.253 55.979 46.592 149.333 46.592 25.771 0 48.896-2.176 69.248-5.675-0.427 3.84-1.707 7.68-1.707 11.52 0 42.667 102.613 85.333 273.792 85.333 160.512 0 273.792-42.667 273.792-85.333 0-3.627-0.469-7.253-0.896-10.88 19.755 3.115 42.496 5.035 68.437 5.035 87.509 0 149.333-23.339 149.333-46.592 0-46.592-58.581-93.099-149.333-93.099zM170.667 762.155c-55.851 0-88.235-8.832-103.125-15.104 10.197-17.28 42.795-39.253 103.125-39.253 47.232 0 78.379 14.976 94.208 30.123-3.584 4.864-7.211 9.685-10.027 14.677-19.285 5.077-47.275 9.557-84.181 9.557zM512 810.667c-92.288 0-149.376-13.312-178.517-23.936 22.229-28.928 81.835-61.397 178.517-61.397 92.544 0 153.173 32.469 176.981 60.8-32.213 11.52-92.245 24.533-176.981 24.533zM853.333 762.155c-38.997 0-65.963-4.395-84.181-9.088-3.072-5.419-6.613-10.752-10.581-16 15.189-14.72 45.696-29.227 94.763-29.227 56.491 0 91.349 21.376 102.571 38.869-16.64 6.955-51.413 15.445-102.571 15.445z"
              ></path>
              <path
                d="M170.667 640c58.923 0 106.667-47.744 106.667-106.667 0-58.837-47.744-106.667-106.667-106.667-58.965 0-106.667 47.829-106.667 106.667 0 58.923 47.701 106.667 106.667 106.667zM170.667 469.333c35.285 0 64 28.715 64 64s-28.715 64-64 64-64-28.715-64-64 28.715-64 64-64z"
              ></path>
            </svg>
            <span class="leftsidebarinner-text04">
              <span>Teams</span>
              <br />
            </span>
          </router-link>
        </div>
        <div class="leftsidebarinner-container5">
          <router-link
            :to="`/projects/${this.$store.state.user.id}`"
            class="leftsidebarinner-navlink4 button"
          >
            <svg viewBox="0 0 1024 1024" class="leftsidebarinner-icon09">
              <path
                d="M768 256h-256c0-47.104-38.229-85.333-85.333-85.333h-170.667c-70.571 0-128 57.429-128 128v426.667c0 70.571 57.429 128 128 128h512c70.571 0 128-57.429 128-128v-341.333c0-70.571-57.429-128-128-128zM256 256h170.667c0 47.104 38.229 85.333 85.333 85.333h256c23.552 0 42.667 19.115 42.667 42.667h-597.333v-85.333c0-23.552 19.115-42.667 42.667-42.667zM768 768h-512c-23.552 0-42.667-19.115-42.667-42.667v-298.667h597.333v298.667c0 23.552-19.115 42.667-42.667 42.667z"
              ></path>
            </svg>
            <span class="leftsidebarinner-text07">{{ text4 }}</span>
          </router-link>
        </div>
        <div class="leftsidebarinner-container6">
          <router-link to="/library" class="leftsidebarinner-navlink5 button">
            <svg viewBox="0 0 1152 1024" class="leftsidebarinner-icon11">
              <path
                d="M224 128h-192c-17.6 0-32 14.4-32 32v704c0 17.6 14.4 32 32 32h192c17.6 0 32-14.4 32-32v-704c0-17.6-14.4-32-32-32zM192 320h-128v-64h128v64z"
              ></path>
              <path
                d="M544 128h-192c-17.6 0-32 14.4-32 32v704c0 17.6 14.4 32 32 32h192c17.6 0 32-14.4 32-32v-704c0-17.6-14.4-32-32-32zM512 320h-128v-64h128v64z"
              ></path>
              <path
                d="M765.088 177.48l-171.464 86.394c-15.716 7.918-22.096 27.258-14.178 42.976l287.978 571.548c7.918 15.718 27.258 22.098 42.976 14.178l171.464-86.392c15.716-7.92 22.096-27.26 14.178-42.974l-287.978-571.55c-7.92-15.718-27.26-22.1-42.976-14.18z"
              ></path>
            </svg>
            <span class="leftsidebarinner-text08">
              <span>Library</span>
              <br />
            </span>
          </router-link>
        </div>
      </nav>
    </div>
  </section>
</template>

<script>
export default {
  name: 'Leftsidebarinner',
  props: {
    rootClassName: String,
    text4: {
      type: String,
      default: 'Projects',
    },
    button: {
      type: String,
      default: 'Button',
    },
    text2: {
      type: String,
      default: 'Dashboard',
    },
  },
  computed: {
    userFirstName() {
      return this.$store.state.user.name;
    },
    userUsername() {
      return this.$store.state.user.username;
    },
  },
}
</script>

<style scoped>
.leftsidebarinner-sidebar {
  flex: 1;
  width: 225px;
  height: 100%;
  display: flex;
  align-self: stretch;
  align-items: stretch;
  flex-direction: column;
  justify-content: flex-start;
  background-color: rgba(4, 0, 72, 0.31);
}
.leftsidebarinner-sidebarheader {
  width: 225px;
  height: 76px;
  display: flex;
  align-self: flex-start;
  align-items: center;
  margin-left: 0px;
  padding-top: 10px;
  flex-direction: column;
  padding-bottom: 10px;
  justify-content: center;
  background-color: #d5d5e1;
}
.leftsidebarinner-container {
  width: 199px;
  height: 100%;
  display: flex;
  align-self: center;
  align-items: center;
  flex-direction: column;
  vertical-align: center;
  justify-content: center;
}
.leftsidebarinner-navlink {
  flex: 1;
  height: 100%;
  display: flex;
  padding: 0px;
  align-self: stretch;
  align-items: center;
  border-width: 0px;
  flex-direction: column;
  justify-content: center;
  text-decoration: none;
  background-color: transparent;
}
.leftsidebarinner-text {
  font-size: 20px;
  align-self: center;
  font-style: normal;
  text-align: center;
  font-weight: 600;
  margin-left: 0px;
  margin-bottom: 0px;
}
.leftsidebarinner-text01 {
  color: var(--dl-color-gray-500);
  align-self: center;
  text-align: center;
  margin-left: 0px;
  margin-bottom: 0px;
}
.leftsidebarinner-container1 {
  width: 225px;
  display: flex;
  align-items: flex-start;
  flex-direction: column;
  justify-content: flex-start;
}
.leftsidebarinner-nav {
  flex: 1;
  width: 199px;
  display: flex;
  align-self: center;
  align-items: center;
  padding-top: 10px;
  flex-direction: column;
  justify-content: flex-start;
  background-color: transparent;
}
.leftsidebarinner-container2 {
  flex: 0 0 auto;
  width: auto;
  height: auto;
  display: flex;
  align-self: flex-start;
  align-items: flex-start;
  padding-top: 5px;
  padding-bottom: 5px;
  justify-content: center;
  background-color: transparent;
}
.leftsidebarinner-navlink1 {
  height: 50px;
  display: flex;
  position: relative;
  align-self: center;
  margin-top: 0px;
  text-align: left;
  font-family: "Arial Black";
  padding-top: 2px;
  border-width: 0px;
  margin-bottom: 0px;
  flex-direction: row;
  padding-bottom: 2px;
  text-decoration: none;
  background-color: transparent;
}
.leftsidebarinner-icon {
  width: 40px;
  height: 40px;
  align-self: center;
  margin-top: 0px;
  padding-top: 2px;
  margin-bottom: 0px;
  padding-bottom: 2px;
  background-color: transparent;
}
.leftsidebarinner-text02 {
  font-size: 22px;
  align-self: center;
  font-style: normal;
  text-align: left;
  font-family: "Inter";
  font-weight: 700;
  margin-left: 8px;
}
.leftsidebarinner-container3 {
  flex: 0 0 auto;
  width: auto;
  height: auto;
  display: flex;
  align-self: flex-start;
  align-items: flex-start;
  padding-top: 5px;
  padding-bottom: 5px;
  justify-content: center;
  background-color: transparent;
}
.leftsidebarinner-navlink2 {
  height: 50px;
  display: flex;
  position: relative;
  align-self: center;
  margin-top: 0px;
  text-align: left;
  font-family: "Arial Black";
  padding-top: 2px;
  border-width: 0px;
  margin-bottom: 0px;
  flex-direction: row;
  padding-bottom: 2px;
  text-decoration: none;
  background-color: transparent;
}
.leftsidebarinner-icon02 {
  width: 40px;
  height: 40px;
  align-self: center;
  margin-top: 0px;
  padding-top: 2px;
  margin-bottom: 0px;
  padding-bottom: 2px;
  background-color: transparent;
}
.leftsidebarinner-text03 {
  font-size: 22px;
  align-self: center;
  font-style: normal;
  text-align: left;
  font-family: "Inter";
  font-weight: 700;
  margin-left: 8px;
}
.leftsidebarinner-container4 {
  flex: 0 0 auto;
  width: auto;
  height: auto;
  display: flex;
  align-self: flex-start;
  align-items: flex-start;
  padding-top: 5px;
  padding-bottom: 5px;
  justify-content: center;
  background-color: transparent;
}
.leftsidebarinner-navlink3 {
  height: 50px;
  position: relative;
  align-self: center;
  margin-top: 0px;
  text-align: left;
  font-family: "Arial Black";
  padding-top: 2px;
  border-width: 0px;
  margin-bottom: 0px;
  padding-bottom: 2px;
  text-decoration: none;
  background-color: transparent;
}
.leftsidebarinner-icon04 {
  width: 40px;
  height: 40px;
  align-self: center;
  margin-top: 0px;
  padding-top: 2px;
  margin-bottom: 0px;
  padding-bottom: 2px;
  background-color: transparent;
}
.leftsidebarinner-text04 {
  font-size: 22px;
  font-style: normal;
  text-align: left;
  font-family: "Inter";
  font-weight: 700;
  margin-left: 8px;
}
.leftsidebarinner-container5 {
  flex: 0 0 auto;
  width: auto;
  height: auto;
  display: flex;
  align-self: flex-start;
  align-items: flex-start;
  padding-top: 5px;
  padding-bottom: 5px;
  justify-content: center;
  background-color: transparent;
}
.leftsidebarinner-navlink4 {
  height: 50px;
  display: flex;
  position: relative;
  align-self: center;
  margin-top: 0px;
  text-align: left;
  font-family: "Arial Black";
  padding-top: 2px;
  border-width: 0px;
  margin-bottom: 0px;
  flex-direction: row;
  padding-bottom: 2px;
  text-decoration: none;
  background-color: transparent;
}
.leftsidebarinner-icon09 {
  width: 40px;
  height: 40px;
  align-self: center;
  margin-top: 0px;
  padding-top: 2px;
  margin-bottom: 0px;
  padding-bottom: 2px;
  background-color: transparent;
}
.leftsidebarinner-text07 {
  font-size: 22px;
  align-self: center;
  font-style: normal;
  text-align: left;
  font-family: "Inter";
  font-weight: 700;
  margin-left: 8px;
}
.leftsidebarinner-container6 {
  flex: 0 0 auto;
  width: auto;
  height: auto;
  display: flex;
  align-self: flex-start;
  align-items: flex-start;
  padding-top: 5px;
  padding-bottom: 5px;
  justify-content: center;
  background-color: transparent;
}
.leftsidebarinner-navlink5 {
  height: 50px;
  display: flex;
  position: relative;
  align-self: center;
  margin-top: 0px;
  text-align: left;
  font-family: "Arial Black";
  padding-top: 2px;
  border-width: 0px;
  margin-bottom: 0px;
  flex-direction: row;
  padding-bottom: 2px;
  text-decoration: none;
  background-color: transparent;
}
.leftsidebarinner-icon11 {
  width: 40px;
  height: 40px;
  align-self: center;
}
.leftsidebarinner-text08 {
  font-size: 22px;
  align-self: center;
  font-style: normal;
  text-align: left;
  font-family: "Inter";
  font-weight: 700;
  margin-left: 8px;
}
.leftsidebarinner-root-class-name {
  top: 75px;
  left: 0px;
  bottom: 0px;
  position: absolute;
}
.leftsidebarinner-root-class-name1 {
  top: 75px;
  left: 0px;
  bottom: 0px;
  position: absolute;
}
.leftsidebarinner-root-class-name2 {
  top: 75px;
  left: 0px;
  bottom: 0px;
  position: absolute;
}
.leftsidebarinner-root-class-name3 {
  top: 75px;
  left: 0px;
  bottom: 0px;
  position: absolute;
}
.leftsidebarinner-root-class-name4 {
  top: 75px;
  left: 0px;
  bottom: 0px;
  position: absolute;
}
.leftsidebarinner-root-class-name5 {
  top: 75px;
  left: 0px;
  bottom: 0px;
  position: absolute;
}
.leftsidebarinner-root-class-name6 {
  top: 75px;
  flex: 1;
  left: 0px;
  bottom: 0px;
  position: static;
  align-self: flex-start;
}
@media(max-width: 991px) {
  .leftsidebarinner-sidebarheader {
    padding-left: var(--dl-space-space-halfunit);
    padding-right: var(--dl-space-space-halfunit);
  }
}
@media(max-width: 479px) {
  .leftsidebarinner-sidebarheader {
    width: auto;
    align-self: stretch;
    align-items: center;
    justify-content: center;
  }
  .leftsidebarinner-container {
    align-self: center;
    align-items: center;
    justify-content: center;
  }
}
</style>