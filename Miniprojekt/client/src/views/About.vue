<template>
  <div class="full-page">
    <div :class="{'animated fadeIn': lazyLoad}">
      <section v-scroll-reveal.reset class="container-box">
        <!-- eslint-disable-next-line vue/no-v-html -->
        <div class="container columns text-left mx-auto pt-5">
          <div class="content column content-box">
            <h1 class="title is-size-1 is-size-2-mobile">Machine Learning</h1>
            <hr />
            <div class="columns is-mobile is-vcentered">
              <div
                :style="{ backgroundImage: 'url(' +
                avatar + ')' }"
                class="avatar column is-narrow"
              />
              <div class="column">
                <p
                  class="is-size-4 is-size-5-mobile
                  has-text-weight-semibold is-family-monospace avatar-text"
                >Thomas, Samuel och Per</p>
                <p
                  class="is-size-6 is-size-7-mobile
                  has-text-weight-semibold is-family-monospace avatar-text"
                >9 December, 2019</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section
        v-scroll-reveal.reset
        :style="{ backgroundImage:
        'linear-gradient(rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0.2)), url(' + contentImageUrl + ')' }"
        class="hero is-info is-fullheight bg-image"
      />

      <section class="section container-box">
        <hr />
        <div class="container columns is-fluid">
          <div class="content column is-three-fifths is-offset-one-fifth content-box content-text">
            <vue-markdown>{{ markdown }}</vue-markdown>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<script>
import moment from 'moment';
import VueMarkdown from 'vue-markdown';
import markdown from '../../README.md';

export default {
  filters: {
    formatDate(value) {
      return moment(String(value)).format('lll');
    },
  },
  components: {
    'vue-markdown': VueMarkdown,
    markdown,
  },
  data() {
    return {
      lazyLoad: false,
      shortName: 'flashcms',
      id: 'unique',
      content: '```Hello <br> ',
      contentImageUrl: 'https://i.ytimg.com/vi/jpsGLsaZKS0/maxresdefault.jpg',
      avatar: 'https://liu.se/-/media/liu/2016/04/06/iStock_000009459009_Large.jpg?la=sv-se&w=640&hash=5B9826D18E1B93A7C3D6BE13FFA4786978A1A957',
    };
  },
};
</script>

<style lang="scss" scoped>
$border-radius-size: 14px;

*,
*:before,
*:after {
  box-sizing: border-box;
}

.hidden {
  visibility: hidden;
}

.avatar {
  width: 70px;
  height: 70px;
  border-radius: 50%;

  background-repeat: no-repeat;
  background-position: center center;
  background-size: cover;
}

.avatar-text {
  margin-bottom: 0 !important;
}

.content-text {
  font-size: 20px;
  line-height: 40px;
}

.container-box {
  height: 300px;
}

.bg-image {
  background-position: center;
  background-size: cover;
  height: 500px;
}
</style>
