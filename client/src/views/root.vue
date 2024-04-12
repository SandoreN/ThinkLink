<template>
  <div class="root-container"
    ><div data-role="Header" class="root-header-container"
      ><header class="root-header"
        ><div class="root-logo"
          ><router-link to="/dashboard" class="root-navlink button"
            ><img
              alt="image"
              src="/thinklink-200h.png"
              class="root-image"
            />Button</router-link
          ></div
        ><div class="root-container01"
          ><div class="root-menu"
            ><span class="root-text">About</span
            ><span class="root-text01">Products</span
            ><span class="root-text02">Pricing</span
            ><span class="root-text03">Blog</span
            ><span class="root-text04">Jobs</span></div
          ><div class="root-container02"
            ><app-registerbuttoncontainer></app-registerbuttoncontainer></div></div></header></div
    ><div class="root-main"
      ><div class="root-blur-background"></div
      ><div class="root-hero"
        ><div class="root-container03"
          ><h1 class="root-text05 Headline1"
            ><span>Work together.</span><br /><span>Get more done.</span></h1
          ><primary-button
            button="Get Started"
            class="root-component01"
          ></primary-button></div
        ><img
          alt="image"
          src="/external/iphonex-1200w-1500h.png"
          class="root-image1" /></div
      ><img
        alt="image"
        src="/external/turquoise-circle.svg"
        class="root-turquoise-cirble" /><img
        alt="image"
        src="/external/purple-circle.svg"
        class="root-purple-circle" /><img
        alt="image"
        src="/external/left.svg"
        class="root-left" /><img
        alt="image"
        src="/external/right.svg"
        class="root-right" /></div
    ><div class="root-clients"
      ><div class="root-divider"></div
      ><img alt="image" src="/external/logo-1.svg" class="root-image2" /><img
        alt="image"
        src="/external/logo-4.svg"
        class="root-image3" /><img
        alt="image"
        src="/external/logo-3.svg"
        class="root-image4" /><img
        alt="image"
        src="/external/logo-5.svg"
        class="root-image5" /><img
        alt="image"
        src="/external/logo-6.svg"
        class="root-image6" /><div class="root-divider1"></div></div
    ><div class="root-features"
      ><h2 class="Headline2 root-text09">Tailor-made features</h2
      ><span class="root-text10"
        ><span class="root-text11"
          >Lorem ipsum is common placeholder text used to demonstrate the graphic
          elements of a document or visual presentation.</span
        ></span
      ><div class="root-features1"
        ><feature-card1 cardTitle="Share"></feature-card1
        ><feature-card1
          imageSrc="/external/02.svg"
          cardTitle="Collaborate"
        ></feature-card1
        ><feature-card1
          imageSrc="/external/03.svg"
          cardTitle="Research"
        ></feature-card1
        ><feature-card1
          imageSrc="/external/04.svg"
          cardTitle="Navigate"
        ></feature-card1
        ><feature-card1
          imageSrc="/external/05.svg"
          cardTitle="Visualize"
        ></feature-card1
        ><feature-card1
          imageSrc="/external/06.svg"
          cardTitle="Organize"
        ></feature-card1></div></div
    ><div class="root-feature1"
      ><div class="root-container04"></div
      ><div class="root-container05"
        ><h3 class="Headline3">Headline</h3
        ><span class="root-text13 Lead1"
          >Lorem ipsum dolor sit amet, consectetur adipiscing elit. Condimentum
          diam orci pretium a pharetra, feugiat cursus. Dictumst risus, sem
          egestas odio cras adipiscing vulputate. Nisi, risus in suscipit non. Non
          commodo volutpat, pharetra, vel.</span
        ><link-icon-button text="Get Started"></link-icon-button></div></div
    ><div class="root-achievements"
      ><div class="root-container06"
        ><h2 class="root-text14"
          ><span class="root-text15"
            ><span>Our 18 years of <span v-html="rawcfwo"></span></span
            ><span> <span v-html="rawxvvs"></span></span></span
          ><br /><span>achievements</span></h2
        ><span class="root-text20"
          >With our super powers we have reached this</span
        ></div
      ><div class="root-container07"
        ><div class="root-container08"
          ><stats-card
            number="140"
            imageSrc="/external/07.svg"
            description="Countries"
          ></stats-card
          ><stats-card
            number="2 Milion"
            imageSrc="https://aheioqhobo.cloudimg.io/v7/_playground-bucket-v2.teleporthq.io_/f27319f0-cedd-4361-add8-6a7ccf8673b3/e22438ba-90d0-42f8-858a-c66202411bda?org_if_sml=11388&amp;force_format=original"
            description="Users"
          ></stats-card></div
        ><div class="root-container09"
          ><stats-card number="500+" description="Clients"></stats-card
          ><div class="root-container10"
            ><div class="root-container11"></div
            ><stats-card
              number="10,000+"
              imageSrc="/external/01.svg"
              description="Downloads per day"
            ></stats-card></div></div
        ><div class="root-container12"></div></div></div
    ><div class="root-feature2"
      ><div class="root-container13"
        ><h2 class="root-text21"
          ><span class="Headline2 root-text22">Research with peers </span
          ><br /></h2
        ><span class="root-text24 Lead1"
          >Lorem ipsum dolor sit amet, consectetur adipiscing elit. Condimentum
          diam orci pretium a pharetra, feugiat cursus. Dictumst risus, sem
          egestas odio cras adipiscing vulputate. Nisi, risus in suscipit non. Non
          commodo volutpat, pharetra, vel.</span
        ></div
      ></div
    ><div class="root-cta"
      ><div class="root-container14"
        ><div class="root-container15"
          ><h2 class="Headline2 root-text25"
            >Manage your projects from your mobile</h2
          ><span class="root-text26 Lead1"
            >Download the app to manage your projects, keep track of the progress
            and complete tasks without procastinating. Stay on track and complete
            on time!</span
          ><span class="root-text27 Subtitle2"
            ><span class="root-text28">Get the App</span></span
          ><store-banner></store-banner></div
        ><div class="root-container16"></div></div></div
    ><div class="root-footer"
      ><footer class="root-container17"
        ><img
          alt="image"
          src="/external/logotype-light.svg"
          class="root-image7" /><div class="root-container18"
          ><span class="root-text29">About</span
          ><span class="root-text30">Features</span
          ><span class="root-text31">Pricing</span
          ><span class="root-text32">Careers</span
          ><span class="root-text33">Help</span
          ><span class="root-text34">Privacy Policy</span></div
        ><div class="root-divider2"></div
        ><div class="root-container19"
          ><span class="root-text35 Body2"
            >© 2020 Landify UI Kit. All rights reserved</span
          ><div class="root-container20"
            ><div class="root-container21"
              ><svg viewBox="0 0 877.7142857142857 1024" class="root-icon">
                <path
                  d="M585.143 512c0-80.571-65.714-146.286-146.286-146.286s-146.286 65.714-146.286 146.286 65.714 146.286 146.286 146.286 146.286-65.714 146.286-146.286zM664 512c0 124.571-100.571 225.143-225.143 225.143s-225.143-100.571-225.143-225.143 100.571-225.143 225.143-225.143 225.143 100.571 225.143 225.143zM725.714 277.714c0 29.143-23.429 52.571-52.571 52.571s-52.571-23.429-52.571-52.571 23.429-52.571 52.571-52.571 52.571 23.429 52.571 52.571zM438.857 152c-64 0-201.143-5.143-258.857 17.714-20 8-34.857 17.714-50.286 33.143s-25.143 30.286-33.143 50.286c-22.857 57.714-17.714 194.857-17.714 258.857s-5.143 201.143 17.714 258.857c8 20 17.714 34.857 33.143 50.286s30.286 25.143 50.286 33.143c57.714 22.857 194.857 17.714 258.857 17.714s201.143 5.143 258.857-17.714c20-8 34.857-17.714 50.286-33.143s25.143-30.286 33.143-50.286c22.857-57.714 17.714-194.857 17.714-258.857s5.143-201.143-17.714-258.857c-8-20-17.714-34.857-33.143-50.286s-30.286-25.143-50.286-33.143c-57.714-22.857-194.857-17.714-258.857-17.714zM877.714 512c0 60.571 0.571 120.571-2.857 181.143-3.429 70.286-19.429 132.571-70.857 184s-113.714 67.429-184 70.857c-60.571 3.429-120.571 2.857-181.143 2.857s-120.571 0.571-181.143-2.857c-70.286-3.429-132.571-19.429-184-70.857s-67.429-113.714-70.857-184c-3.429-60.571-2.857-120.571-2.857-181.143s-0.571-120.571 2.857-181.143c3.429-70.286 19.429-132.571 70.857-184s113.714-67.429 184-70.857c60.571-3.429 120.571-2.857 181.143-2.857s120.571-0.571 181.143 2.857c70.286 3.429 132.571 19.429 184 70.857s67.429 113.714 70.857 184c3.429 60.571 2.857 120.571 2.857 181.143z"
                ></path></svg></div
            ><div class="root-container22"
              ><svg viewBox="0 0 877.7142857142857 1024" class="root-icon2">
                <path
                  d="M585.143 857.143c-5.714-33.143-27.429-147.429-80-284.571-0.571 0-1.714 0.571-2.286 0.571 0 0-222.286 77.714-294.286 234.286-3.429-2.857-8.571-6.286-8.571-6.286 65.143 53.143 148 85.714 238.857 85.714 52 0 101.143-10.857 146.286-29.714zM479.429 510.286c-9.143-21.143-19.429-42.286-30.286-63.429-193.143 57.714-378.286 53.143-384.571 53.143-0.571 4-0.571 8-0.571 12 0 96 36.571 184 96 250.286v0c102.286-182.286 304.571-247.429 304.571-247.429 5.143-1.714 10.286-2.857 14.857-4.571zM418.286 389.143c-65.143-115.429-134.286-209.143-139.429-216-104.571 49.143-182.286 145.714-206.857 261.714 9.714 0 166.286 1.714 346.286-45.714zM809.143 571.429c-8-2.286-112.571-35.429-233.714-16.571 49.143 135.429 69.143 245.714 73.143 268 84-56.571 143.429-146.857 160.571-251.429zM349.143 148c-0.571 0-0.571 0-1.143 0.571 0 0 0.571-0.571 1.143-0.571zM686.286 230.857c-65.714-58.286-152.571-93.714-247.429-93.714-30.286 0-60 4-88.571 10.857 5.714 7.429 76.571 100.571 140.571 218.286 141.143-52.571 194.286-133.714 195.429-135.429zM813.714 508c-1.143-88.571-32.571-170.286-85.143-234.286-1.143 1.143-61.143 88-209.143 148.571 8.571 17.714 17.143 36 25.143 54.286 2.857 6.286 5.143 13.143 8 19.429 129.143-16.571 256.571 11.429 261.143 12zM877.714 512c0 242.286-196.571 438.857-438.857 438.857s-438.857-196.571-438.857-438.857 196.571-438.857 438.857-438.857 438.857 196.571 438.857 438.857z"
                ></path></svg></div
            ><div class="root-container23"
              ><svg viewBox="0 0 950.8571428571428 1024" class="root-icon4">
                <path
                  d="M925.714 233.143c-25.143 36.571-56.571 69.143-92.571 95.429 0.571 8 0.571 16 0.571 24 0 244-185.714 525.143-525.143 525.143-104.571 0-201.714-30.286-283.429-82.857 14.857 1.714 29.143 2.286 44.571 2.286 86.286 0 165.714-29.143 229.143-78.857-81.143-1.714-149.143-54.857-172.571-128 11.429 1.714 22.857 2.857 34.857 2.857 16.571 0 33.143-2.286 48.571-6.286-84.571-17.143-148-91.429-148-181.143v-2.286c24.571 13.714 53.143 22.286 83.429 23.429-49.714-33.143-82.286-89.714-82.286-153.714 0-34.286 9.143-65.714 25.143-93.143 90.857 112 227.429 185.143 380.571 193.143-2.857-13.714-4.571-28-4.571-42.286 0-101.714 82.286-184.571 184.571-184.571 53.143 0 101.143 22.286 134.857 58.286 41.714-8 81.714-23.429 117.143-44.571-13.714 42.857-42.857 78.857-81.143 101.714 37.143-4 73.143-14.286 106.286-28.571z"
                ></path></svg></div
            ><div class="root-container24"
              ><svg viewBox="0 0 1024 1024" class="root-icon6">
                <path
                  d="M406.286 644.571l276.571-142.857-276.571-144.571v287.429zM512 152c215.429 0 358.286 10.286 358.286 10.286 20 2.286 64 2.286 102.857 43.429 0 0 31.429 30.857 40.571 101.714 10.857 82.857 10.286 165.714 10.286 165.714v77.714s0.571 82.857-10.286 165.714c-9.143 70.286-40.571 101.714-40.571 101.714-38.857 40.571-82.857 40.571-102.857 42.857 0 0-142.857 10.857-358.286 10.857v0c-266.286-2.286-348-10.286-348-10.286-22.857-4-74.286-2.857-113.143-43.429 0 0-31.429-31.429-40.571-101.714-10.857-82.857-10.286-165.714-10.286-165.714v-77.714s-0.571-82.857 10.286-165.714c9.143-70.857 40.571-101.714 40.571-101.714 38.857-41.143 82.857-41.143 102.857-43.429 0 0 142.857-10.286 358.286-10.286v0z"
                ></path></svg></div></div></div></footer></div
  ></div>
</template>

<script>
import AppRegisterbuttoncontainer from '../components/registerbuttoncontainer'
import PrimaryButton from '../components/primary-button'
import FeatureCard1 from '../components/feature-card1'
import LinkIconButton from '../components/link-icon-button'
import StatsCard from '../components/stats-card'
import StoreBanner from '../components/store-banner'

export default {
  name: 'Root',
  props: {},
  components: {
    AppRegisterbuttoncontainer,
    PrimaryButton,
    FeatureCard1,
    LinkIconButton,
    StatsCard,
    StoreBanner,
  },
  data() {
    return {
      rawcfwo: ' ',
      rawxvvs: ' ',
    }
  },
  metaInfo: {
    title: 'ThinkLink - Home',
    meta: [
      {
        property: 'og:title',
        content: 'ThinkLink - Home',
      },
      {
        name: 'robots',
        content: 'noindex',
      },
    ],
  },
}
</script>

<style scoped>
.root-container {
  width: 100%;
  display: flex;
  overflow: auto;
  min-height: 100vh;
  align-items: center;
  flex-direction: column;
}
.root-header-container {
  width: 100%;
  display: flex;
  align-self: flex-start;
  align-items: stretch;
  flex-direction: column;
  justify-content: center;
}
.root-header {
  flex: 0 0 auto;
  width: 100%;
  height: 75px;
  display: flex;
  z-index: 100;
  position: relative;
  max-width: auto;
  align-self: flex-start;
  align-items: center;
  flex-direction: row;
  justify-content: flex-start;
}
.root-logo {
  display: flex;
  position: relative;
  align-self: stretch;
  align-items: center;
  flex-direction: row;
  justify-content: space-between;
}
.root-navlink {
  flex: 1;
  color: transparent;
  width: 225px;
  height: 100%;
  align-self: flex-start;
  border-width: 0px;
  border-radius: 0px;
  text-decoration: none;
}
.root-image {
  top: 0px;
  left: 0px;
  right: 0px;
  width: 200px;
  bottom: 0px;
  margin: auto;
  position: absolute;
  align-self: center;
  object-fit: cover;
}
.root-container01 {
  flex: 1;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}
.root-menu {
  flex: 1;
  width: auto;
  display: flex;
  flex-wrap: wrap;
  align-self: center;
  align-items: stretch;
  flex-direction: row;
  justify-content: center;
}
.root-text {
  transition: 0.3s;
  margin-right: var(--dl-space-space-doubleunit);
}
.root-text:hover {
  color: var(--dl-color-turquoise-default);
}
.root-text01 {
  transition: 0.3s;
  margin-right: var(--dl-space-space-doubleunit);
}
.root-text01:hover {
  color: var(--dl-color-turquoise-default);
}
.root-text02 {
  transition: 0.3s;
  margin-right: var(--dl-space-space-doubleunit);
}
.root-text02:hover {
  color: var(--dl-color-turquoise-default);
}
.root-text03 {
  transition: 0.3s;
  margin-right: var(--dl-space-space-doubleunit);
}
.root-text03:hover {
  color: var(--dl-color-turquoise-default);
}
.root-text04 {
  transition: 0.3s;
  margin-right: var(--dl-space-space-doubleunit);
}
.root-text04:hover {
  color: var(--dl-color-turquoise-default);
}
.root-container02 {
  width: 225px;
  height: 100%;
  display: flex;
  align-self: flex-end;
  align-items: center;
  justify-content: center;
}
.root-main {
  width: 100%;
  display: flex;
  position: relative;
  align-items: center;
  flex-direction: column;
}
.root-blur-background {
  top: 0px;
  left: auto;
  right: 0px;
  width: 100%;
  bottom: auto;
  filter: blur(60px);
  height: 70vh;
  display: flex;
  position: absolute;
  align-items: center;
  flex-direction: column;
  background-color: #f2f2f2;
}
.root-hero {
  flex: 0 0 auto;
  width: 92.5%;
  height: 80vh;
  display: flex;
  padding: var(--dl-space-space-doubleunit);
  z-index: 100;
  max-width: auto;
  align-items: center;
  flex-direction: row;
  justify-content: space-between;
}
.root-container03 {
  flex: 0 0 auto;
  width: auto;
  height: auto;
  display: flex;
  align-items: flex-start;
  flex-direction: column;
}
.root-text05 {
  margin-bottom: var(--dl-space-space-doubleunit);
}
.root-component01 {
  text-decoration: none;
}
.root-image1 {
  width: 320px;
  object-fit: cover;
}
.root-turquoise-cirble {
  top: 439px;
  left: auto;
  right: 430px;
  width: 170px;
  bottom: auto;
  filter: blur(60px);
  opacity: 0.6;
  position: absolute;
  object-fit: cover;
}
.root-purple-circle {
  top: -14px;
  right: 84px;
  width: 400px;
  filter: blur(60px);
  opacity: 0.4;
  position: absolute;
  object-fit: cover;
}
.root-left {
  top: 653px;
  left: 0px;
  right: auto;
  width: 420px;
  bottom: auto;
  position: absolute;
  object-fit: cover;
}
.root-right {
  top: 441px;
  left: auto;
  right: 0px;
  width: 612px;
  bottom: auto;
  position: absolute;
  object-fit: cover;
}
.root-clients {
  flex: 0 0 auto;
  width: 100%;
  display: flex;
  z-index: 100;
  overflow: hidden;
  position: relative;
  flex-wrap: wrap;
  max-width: 1110px;
  align-items: center;
  padding-top: var(--dl-space-space-doubleunit);
  padding-left: var(--dl-space-space-doubleunit);
  padding-right: var(--dl-space-space-doubleunit);
  flex-direction: row;
  padding-bottom: var(--dl-space-space-doubleunit);
  justify-content: space-between;
}
.root-divider {
  top: 0px;
  left: auto;
  right: auto;
  width: 100%;
  bottom: auto;
  height: 1px;
  position: absolute;
  background: linear-gradient(90deg, rgba(192, 204, 218, 0.1) 0%, rgba(192, 204, 218, 0.6) 50.38%, rgba(192, 204, 218, 0.1) 100%);;
}
.root-image2 {
  width: 100px;
  object-fit: cover;
}
.root-image3 {
  width: 100px;
  object-fit: cover;
}
.root-image4 {
  width: 100px;
  object-fit: cover;
}
.root-image5 {
  width: 100px;
  object-fit: cover;
}
.root-image6 {
  width: 100px;
  object-fit: cover;
}
.root-divider1 {
  top: auto;
  left: auto;
  right: auto;
  width: 100%;
  bottom: 0px;
  height: 1px;
  position: absolute;
  background: linear-gradient(90deg, rgba(192, 204, 218, 0.1) 0%, rgba(192, 204, 218, 0.6) 50.38%, rgba(192, 204, 218, 0.1) 100%);;
}
.root-features {
  flex: 0 0 auto;
  width: 100%;
  display: flex;
  padding: var(--dl-space-space-doubleunit);
  z-index: 100;
  max-width: 1110px;
  align-items: center;
  flex-direction: column;
  justify-content: flex-start;
}
.root-text10 {
  max-width: 500px;
  text-align: center;
}
.root-text11 {
  white-space: pre-wrap;
}
.root-features1 {
  display: flex;
  flex-wrap: wrap;
  margin-top: var(--dl-space-space-doubleunit);
  align-items: center;
  flex-direction: row;
  justify-content: center;
}
.root-feature1 {
  flex: 0 0 auto;
  width: 100%;
  display: flex;
  padding: var(--dl-space-space-doubleunit);
  z-index: 100;
  max-width: 1110px;
  align-items: center;
  flex-direction: row;
  justify-content: center;
}
.root-container04 {
  flex: 0 0 auto;
  width: 540px;
  border: 2px dashed rgba(120, 120, 120, 0.4);
  height: 540px;
  display: flex;
  overflow: hidden;
  align-items: center;
  flex-direction: column;
  justify-content: center;
  background-color: var(--dl-color-purple-100);
}
.root-container05 {
  flex: 1;
  margin: var(--dl-space-space-doubleunit);
  display: flex;
  align-items: flex-start;
  flex-direction: column;
  justify-content: flex-start;
}
.root-text13 {
  max-width: 400px;
  margin-top: var(--dl-space-space-doubleunit);
  margin-bottom: var(--dl-space-space-doubleunit);
}
.root-achievements {
  flex: 0 0 auto;
  width: 100%;
  display: flex;
  padding: var(--dl-space-space-doubleunit);
  z-index: 100;
  flex-wrap: wrap;
  max-width: 1110px;
  align-items: center;
  flex-direction: row;
  justify-content: flex-start;
}
.root-container06 {
  flex: 0 0 auto;
  display: flex;
  align-items: flex-start;
  flex-direction: column;
  justify-content: flex-start;
}
.root-text15 {
  white-space: pre-wrap;
}
.root-container07 {
  flex: 1;
  display: flex;
  align-items: center;
  flex-direction: column;
  justify-content: center;
}
.root-container08 {
  flex: 0 0 auto;
  width: auto;
  height: auto;
  display: flex;
  align-items: flex-start;
  justify-content: center;
}
.root-container09 {
  flex: 0 0 auto;
  width: auto;
  height: auto;
  display: flex;
  align-items: flex-start;
  justify-content: center;
}
.root-container10 {
  flex: 0 0 auto;
  width: auto;
  height: auto;
  display: flex;
  align-items: flex-start;
  justify-content: center;
}
.root-container11 {
  border: 2px dashed rgba(120, 120, 120, 0.4);
  display: flex;
  align-items: center;
  flex-direction: row;
  justify-content: center;
}
.root-container12 {
  border: 2px dashed rgba(120, 120, 120, 0.4);
  display: flex;
  align-items: center;
  flex-direction: row;
  justify-content: center;
}
.root-feature2 {
  flex: 0 0 auto;
  width: 100%;
  display: flex;
  padding: var(--dl-space-space-doubleunit);
  z-index: 100;
  max-width: 1110px;
  align-items: center;
  flex-direction: column;
  justify-content: flex-start;
}
.root-container13 {
  display: flex;
  align-items: center;
  flex-direction: row;
  justify-content: flex-start;
}
.root-text24 {
  max-width: 400px;
  margin-top: var(--dl-space-space-doubleunit);
  margin-bottom: var(--dl-space-space-doubleunit);
}
.root-cta {
  width: 100%;
  display: flex;
  overflow: hidden;
  align-items: center;
  flex-direction: column;
  justify-content: center;
  background-color: var(--dl-color-turquoise-default);
}
.root-container14 {
  flex: 0 0 auto;
  width: 100%;
  display: flex;
  padding: var(--dl-space-space-doubleunit);
  z-index: 100;
  flex-wrap: wrap;
  max-width: 1110px;
  align-items: center;
  flex-direction: row;
  justify-content: flex-start;
}
.root-container15 {
  flex: 1;
  display: flex;
  align-items: flex-start;
  flex-direction: column;
  justify-content: flex-start;
}
.root-text26 {
  max-width: 500px;
}
.root-text27 {
  max-width: 400px;
  margin-top: var(--dl-space-space-doubleunit);
  margin-bottom: var(--dl-space-space-halfunit);
}
.root-text28 {
  white-space: pre-wrap;
}
.root-container16 {
  width: 520px;
  border: 2px dashed rgba(120, 120, 120, 0.4);
  display: flex;
  position: relative;
  align-items: center;
  flex-direction: row;
  justify-content: flex-start;
}
.root-footer {
  flex: 0 0 auto;
  color: var(--dl-color-gray-white);
  width: 100%;
  display: flex;
  align-items: flex-start;
  flex-direction: row;
  justify-content: center;
  background-color: var(--dl-color-gray-black);
}
.root-container17 {
  flex: 0 0 auto;
  width: 100%;
  display: flex;
  padding: var(--dl-space-space-doubleunit);
  z-index: 100;
  flex-wrap: wrap;
  max-width: 1110px;
  align-items: center;
  flex-direction: column;
  justify-content: space-between;
}
.root-image7 {
  object-fit: cover;
}
.root-container18 {
  display: flex;
  margin-top: var(--dl-space-space-doubleunit);
  align-items: center;
  margin-bottom: var(--dl-space-space-doubleunit);
  flex-direction: row;
  justify-content: flex-start;
}
.root-text29 {
  transition: 0.3s;
  margin-right: var(--dl-space-space-unit);
}
.root-text29:hover {
  color: var(--dl-color-turquoise-default);
}
.root-text30 {
  transition: 0.3s;
  margin-right: var(--dl-space-space-unit);
}
.root-text30:hover {
  color: var(--dl-color-turquoise-default);
}
.root-text31 {
  transition: 0.3s;
  margin-right: var(--dl-space-space-unit);
}
.root-text31:hover {
  color: var(--dl-color-turquoise-default);
}
.root-text32 {
  transition: 0.3s;
  margin-right: var(--dl-space-space-unit);
}
.root-text32:hover {
  color: var(--dl-color-turquoise-default);
}
.root-text33 {
  transition: 0.3s;
  margin-right: var(--dl-space-space-unit);
}
.root-text33:hover {
  color: var(--dl-color-turquoise-default);
}
.root-text34 {
  transition: 0.3s;
  white-space: nowrap;
}
.root-text34:hover {
  color: var(--dl-color-turquoise-default);
}
.root-divider2 {
  width: 100%;
  height: 1px;
  opacity: 0.2;
  background-color: var(--dl-color-gray-white);
}
.root-container19 {
  width: 100%;
  display: flex;
  margin-top: var(--dl-space-space-unit);
  align-items: center;
  flex-direction: row;
  justify-content: space-between;
}
.root-text35 {
  color: var(--dl-color-gray-300);
  margin-top: var(--dl-space-space-unit);
}
.root-container20 {
  flex: 0 0 auto;
  width: 200px;
  display: flex;
  align-items: flex-start;
  flex-direction: row;
}
.root-container21 {
  display: flex;
  padding: var(--dl-space-space-halfunit);
  align-items: flex-start;
  border-radius: var(--dl-radius-radius-round);
  flex-direction: column;
  background-color: var(--dl-color-gray-900);
}
.root-icon {
  fill: var(--dl-color-gray-white);
  width: var(--dl-size-size-unit);
  height: var(--dl-size-size-unit);
  transition: 0.3s;
}
.root-icon:hover {
  fill: var(--dl-color-purple-default);
}
.root-container22 {
  display: flex;
  padding: var(--dl-space-space-halfunit);
  align-items: flex-start;
  margin-left: var(--dl-space-space-unit);
  border-radius: var(--dl-radius-radius-round);
  flex-direction: column;
  background-color: var(--dl-color-gray-900);
}
.root-icon2 {
  fill: var(--dl-color-gray-white);
  width: var(--dl-size-size-unit);
  height: var(--dl-size-size-unit);
  transition: 0.3s;
}
.root-icon2:hover {
  fill: var(--dl-color-turquoise-default);
}
.root-container23 {
  display: flex;
  padding: var(--dl-space-space-halfunit);
  align-items: flex-start;
  margin-left: var(--dl-space-space-unit);
  border-radius: var(--dl-radius-radius-round);
  flex-direction: column;
  background-color: var(--dl-color-gray-900);
}
.root-icon4 {
  fill: var(--dl-color-gray-white);
  width: var(--dl-size-size-unit);
  height: var(--dl-size-size-unit);
  transition: 0.3s;
}
.root-icon4:hover {
  fill: var(--dl-color-turquoise-default);
}
.root-container24 {
  display: flex;
  padding: var(--dl-space-space-halfunit);
  align-items: flex-start;
  margin-left: var(--dl-space-space-unit);
  border-radius: var(--dl-radius-radius-round);
  flex-direction: column;
  background-color: var(--dl-color-gray-900);
}
.root-icon6 {
  fill: var(--dl-color-gray-white);
  width: var(--dl-size-size-unit);
  height: var(--dl-size-size-unit);
  transition: 0.3s;
}
.root-icon6:hover {
  fill: var(--dl-color-turquoise-default);
}
@media(max-width: 991px) {
  .root-hero {
    height: auto;
    flex-direction: column;
  }
  .root-container03 {
    align-items: center;
    margin-bottom: var(--dl-space-space-doubleunit);
  }
  .root-text05 {
    text-align: center;
  }
  .root-feature1 {
    flex-direction: column;
  }
  .root-container05 {
    margin-left: 0px;
    margin-right: 0px;
  }
  .root-achievements {
    flex-direction: column;
  }
  .root-container07 {
    margin-top: var(--dl-space-space-doubleunit);
  }
  .root-container13 {
    align-items: flex-start;
    flex-direction: column;
  }
  .root-container16 {
    display: none;
  }
}
@media(max-width: 767px) {
  .root-menu {
    display: none;
  }
  .root-text05 {
    font-size: 50px;
    text-align: center;
  }
  .root-clients {
    justify-content: center;
  }
  .root-image2 {
    margin: var(--dl-space-space-unit);
  }
  .root-image3 {
    margin: var(--dl-space-space-unit);
  }
  .root-image4 {
    margin: var(--dl-space-space-unit);
  }
  .root-image5 {
    margin: var(--dl-space-space-unit);
  }
  .root-image6 {
    margin: var(--dl-space-space-unit);
  }
  .root-text09 {
    font-size: 40px;
  }
  .root-text14 {
    font-size: 40px;
  }
  .root-text21 {
    font-size: 40px;
  }
  .root-text22 {
    font-size: 40px;
  }
  .root-text25 {
    font-size: 40px;
  }
  .root-container18 {
    flex-wrap: wrap;
    justify-content: center;
  }
  .root-container19 {
    flex-direction: column;
  }
  .root-text35 {
    margin-top: var(--dl-space-space-unit);
    margin-bottom: var(--dl-space-space-unit);
  }
}
@media(max-width: 479px) {
  .root-text09 {
    text-align: center;
  }
  .root-text10 {
    text-align: center;
  }
  .root-container06 {
    align-items: center;
  }
  .root-text14 {
    text-align: center;
  }
  .root-text20 {
    text-align: center;
  }
  .root-container11 {
    flex-direction: column;
  }
  .root-container12 {
    flex-direction: column;
  }
}
</style>
