# OAuth Stuff

The SS14 authentication hub implements OAuth2 and OpenID Connect. This allows you to do "log in with your Space Station 14 account" stuff. Support for all this is implemented by IdentityServer4 (god bless).

![log-in-with-ss14.png](../assets/images/hosting-log-in-with-ss14.png)

This is used by the [official forum](https://forum.ss14.io), [official wiki](https://wiki.ss14.io) and SS14.Admin panel to make it easy for people to log into stuff with the same account everywhere. I am very pleased with how well it works.

OAuth apps are tied to an SS14 account and can be created [here](https://central.spacestation14.io/web/Identity/Account/Manage/Developer). 

Some information you may want to know (this is repeated on the app management page):
* Authority: https://central.spacestation14.io/web/
* OIDC config: https://central.spacestation14.io/web/.well-known/openid-configuration 
* Allowed authorization flow: Authorization code (implicit etc is not allowed)
* Available scopes: `openid`, `profile`, `email`.

Depending on the library you are using to implement OIDC support, you may have to disable "require PKCE". e.g. the PHP library used by MediaWiki does not support this, so you have to turn it off.

Note that some of these limitations (e.g. no implicit grant) are not for technical reasons. IdentityServer4 has a [*ton*](https://github.com/space-wizards/SS14.Web/blob/618802153e91d258f7b99a9165e0990ca0c59d30/SS14.Web/Areas/Admin/Pages/Clients/Client.cshtml.cs#L46-L99) of buttons and dials we can tweak if need be. If you need anything here that isn't available from the current OAuth app creation menu, do let us know.

```admonish info
If you get errors when trying to test logging in, make sure all information is correct (**especially the redirect URI, check this with your browser's network tab**)

We can provide more detailed error help on request.
```

```admonish warning
IdentityServer4 defaults to being somewhat restrictive with what signing algorithms are supported. This is a problem for things like **PHP/MediaWiki** as OpenID-Connect-PHP does not currently support `ES256`. It is not currently possible for you to change this setting yourself.

We can change this manually through the hub-admin panel (see note about dials above), so if this is a problem for you, tell us.

See the following issue: https://github.com/space-wizards/SS14.Web/issues/11
```