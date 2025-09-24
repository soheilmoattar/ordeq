



    case $1 in
    --git-ref)
        GIT_REFERENCE="$2"
        shift
        ;;
    --target-branch)
        TARGET_BRANCH="$2"
        shift
        ;;
    *)
        echo "Unknown parameter passed: $1"
        exit 1
        ;;
    esac
    shift



    echo "Error: --git-ref argument is required"
    exit 1



    echo "Error: --target-branch argument is required"
    exit 1


















        CHANGED_FOLDERS=$(
            git diff --name-only "$TARGET_BRANCH" HEAD |
                grep '^packages/' |
                cut -d'/' -f2 |
                sort |
                uniq |
                # Only consider the packages that are non-empty
                while read -r pkg; do
                    if [ -d "packages/$pkg" ]; then
                        echo "$pkg"
                    fi
                done |
                tr '\n' ',' |
                sed 's/,$//'
        )



