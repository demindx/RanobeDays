<script setup>

import Logo from '../../assets/icons/icon.svg?component';
import SearchIcon from '../../assets/icons/header/search.svg?component';
import BookmarkIcon from '../../assets/icons/header/book.svg?component';
import NotificationIcon from '../../assets/icons/header/notifications.svg?component';

import Button from '../../components/Button.vue';

const props = defineProps({
  isLoggedIn: Boolean
});


</script>


<template>
  <header class="header">
    <div class="wrapper">

      <a href="#" class="header__logo">
        <RouterLink to="/">
          <Logo class="header__logo-icon" />
        </RouterLink>
      </a>


      <div class="header__nav-bar">

        <div class="header__menu-item">
          <RouterLink to="/catalog">Каталог</RouterLink>
          <!-- <a href="#">Каталог</a> -->
        </div>

        <div class="header__menu-item">
          <a href="#">Случайный тайтл</a>
        </div>

        <div class="header__menu-item">
          <a href="#">Топ</a>
        </div>

      </div>

      <div class="header__search">
        <input type="text" onfocus="this.value=''">
        <SearchIcon />
      </div>

      <div class="header__user">
        <div class="logged-in" v-if="isLoggedIn">
          <BookmarkIcon />
          <NotificationIcon />
          <div class="header__user-icon"></div>
        </div>
        <div class="logged-out" v-if="!isLoggedIn">
          <Button text="Войти" data-size="regular" />
        </div>
      </div>


    </div>
  </header>
</template>


<style lang="scss" scoped>
.wrapper {
  /* Styles for wrapper*/
  width: 1250px;
  margin: 0 auto;
  height: 100%;
}


.header {
  background-color: #161616;
  height: 60px;

  &>.wrapper {
    display: flex;
    justify-content: space-between;
  }

  &__user-icon {
    background-color: $main;
    width: 32px;
    height: 32px;
    border-radius: 100px;
  }

  &__logo {
    margin: auto 0;
    width: 66px;
  }

  &__menu-item {
    /* Styles for header__menu-item */
    margin-right: 40px;

    &>a {
      font-size: 12pt;
      color: $font-main;
      text-decoration: none;
    }
  }

  &__nav-bar {
    /* Styles for header__nav-bar */
    margin: auto 0;
    width: fit-content;
    display: flex;
  }

  &__search {
    /* Styles for header__search */

    display: flex;

    &>svg {
      position: relative;
      right: 30px;
      margin: auto 0;

      &:hover {
        cursor: pointer;
      }
    }

    &>input {

      &:focus {
        outline: none;
      }

      color: $background;


      padding: 10px 33px 10px 10px;

      border-style: none;
      width: 340px;
      height: 25px;
      background-color: $secondary;
      box-shadow: inset 0 0 20px rgba($color: #000000, $alpha: 0.5);
      border-radius: 100px;
    }

    margin: auto 0;
  }


  &__user {
    /* Styles for header__user */
    margin: auto 0;

    &>* {
      display: flex;
    }
  }
}
</style>
