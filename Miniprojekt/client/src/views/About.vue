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

      <section class="container-box container columns text-left mx-auto pt-5">
        <hr />
        <div class="container columns is-fluid">
          <div class="content column is-three-fifths is-offset-one-fifth content-box content-text">
            <h1>Text Summarization using deep learning</h1>
            <p>For this we followed a <a>tutorial</a> which used ... and ... type of dataset...</p>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<script>
import VueEmbedGist from 'vue-embed-gist';

export default {
  components: {
    VueEmbedGist,
  },
  data() {
    return {
      lazyLoad: false,
      shortName: 'flashcms',
      id: 'unique',
      contentImageUrl: 'https://images.idgesg.net/images/article/2018/01/emerging-tech_ai_machine-learning-100748222-large.jpg',
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
