package sharafutdinov.artur.marketplus.model;

import javax.persistence.*;
import java.io.Serializable;
import java.util.HashSet;
import java.util.Set;

/**
 * Created by first on 21.03.17.
 */
@Entity
@Table(name = "USERS")
public class User implements Serializable {

    @Id
    @Column(name = "USER_ID", unique = true, nullable = false)
    private String userId;

    @Column(name = "NAME", nullable = false, length = 32)
    private String name;

    @Column(name = "PASSWORD", nullable = false, length = 64)
    private String password;


    @Column(name = "ACTIVE", nullable = false, length = 1)
    private Integer active;

    @ManyToMany(fetch = FetchType.EAGER,cascade = CascadeType.ALL)
    @JoinTable(
            name = "USER_ROLE",
            joinColumns = @JoinColumn(name = "USER_ID"),
            inverseJoinColumns = @JoinColumn(name = "ROLE_ID")
    )
    private Set<Role> roles = new HashSet<>();

    public User() {
    }

    public User(final String userId, final String name, final String password, final Integer active, final Set<Role> roles) {
        this.userId = userId;
        this.name = name;
        this.password = password;
        this.active = active;
        this.roles = roles;
    }

    public String getUserId() {
        return userId;
    }

    public void setUserId(final String userId) {
        this.userId = userId;
    }

    public String getName() {
        return name;
    }

    public void setName(final String name) {
        this.name = name;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(final String password) {
        this.password = password;
    }

    public Integer getActive() {
        return active;
    }

    public void setActive(final Integer active) {
        this.active = active;
    }

    public Set<Role> getRoles() {
        return roles;
    }

    public void setRoles(final Set<Role> roles) {
        this.roles = roles;
    }


}
