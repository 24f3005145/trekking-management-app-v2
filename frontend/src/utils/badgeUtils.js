export function badgeClass(status) {

    switch (status) {

        case "Open":
            return "bg-success"

        case "Closed":
            return "bg-danger"

        case "Completed":
            return "bg-secondary"

        case "Pending":
            return "bg-warning text-dark"

        default:
            return "bg-primary"

    }

}