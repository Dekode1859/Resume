<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the installation.
 * You don't have to use the web site, you can copy this file to "wp-config.php"
 * and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * Database settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://wordpress.org/documentation/article/editing-wp-config-php/
 *
 * @package WordPress
 */

// ** Database settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'resume_db' );

/** Database username */
define( 'DB_USER', 'root' );

/** Database password */
define( 'DB_PASSWORD', '' );

/** Database hostname */
define( 'DB_HOST', 'localhost' );

/** Database charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8mb4' );

/** The database collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication unique keys and salts.
 *
 * Change these to different unique phrases! You can generate these using
 * the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}.
 *
 * You can change these at any point in time to invalidate all existing cookies.
 * This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define( 'AUTH_KEY',         '(w)4,`zwN(`mo2-?t%^N?E 3+Bm1-f&C|)0&RV*^-1IpH)gw8slrb4v9D:w<~`qN' );
define( 'SECURE_AUTH_KEY',  '?z?ca^(>gOn{AEC,UU;c-$}7K%C%pAUVzaeOrq_8V]AszIc~SeZ`4L<E`.(2i>=m' );
define( 'LOGGED_IN_KEY',    'ue{Q8|gjH%c)`L/p(C/ ;^tqGl~yz1([>`qkES=Li`aOg.EV~cRB~W;$p4bTcYnr' );
define( 'NONCE_KEY',        '#K-iRu#!9DK@=!;gRgKp_E&YL8ao2&|X>6C }+}OGPq!IN(wt sARn1,A)={c/=s' );
define( 'AUTH_SALT',        'R{p=`&1:v.M+nYEzCF}+vGq^(@;2aOb>TK%3MMe>H,53exEFr07_3V|^8.ZH. el' );
define( 'SECURE_AUTH_SALT', 'ZLt8 :{xpZ(]uM[?BNDHYS.DiLn+7<Q-^mr)NHwusmnsN/y!8e!!0.W5MxrBoVun' );
define( 'LOGGED_IN_SALT',   'Fpq3.6$fn2%Uskdhn,1R:v]@Y/B{SaS1O$}q;K<~$E KyJ[R^PaLQMWm}>;tw=F^' );
define( 'NONCE_SALT',       '-9A(xkMH3.F?gthtjaT7.^IP.kD*<snII,xp*:/(zpk*D$0sg?>FutR2kKEb%p,=' );

/**#@-*/

/**
 * WordPress database table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix = 'wp_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the documentation.
 *
 * @link https://wordpress.org/documentation/article/debugging-in-wordpress/
 */
define( 'WP_DEBUG', false );

/* Add any custom values between this line and the "stop editing" line. */



/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __DIR__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
