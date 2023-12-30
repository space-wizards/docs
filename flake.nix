{
  description = "Development environment for Space Station 14";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/release-23.11";

  outputs = { self, nixpkgs }:
    let
      forAllSystems = function:
        nixpkgs.lib.genAttrs [ "x86_64-linux" "aarch64-linux" ]
        (system: function nixpkgs.legacyPackages.${system});
    in {
      devShells = forAllSystems
        (pkgs: { default = import ./shell.nix { inherit pkgs; }; });
    };

}
