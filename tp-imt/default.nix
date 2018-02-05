with import <nixpkgs> {};

let py = python27.withPackages (pkgs: with pkgs; [
  # These are for spacemacs python layer. To get spacemacs with the
  # correct PATH. run nix-shell, then launch Emacs inside this
  # nix-shell.
  virtualenv
]);
in stdenv.mkDerivation {
  name = "tp-imt";
  buildInputs = [ py libffi libressl jq ];
}
