package sharafutdinov.artur.marketplus.demo;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;
import sharafutdinov.artur.marketplus.model.Role;
import sharafutdinov.artur.marketplus.model.User;

import java.io.File;
import java.net.URL;
import java.util.HashSet;

/**
 * Created by first on 21.03.17.
 */
public class HibernateManyToManyDemo {

    public static void main(String[] args) {
        URL url = HibernateManyToManyDemo.class.getClassLoader().getResource("hibernate.cfg.xml");
        File file = new File(url.getPath());

        Configuration configuration = new Configuration().configure(file);
        SessionFactory sessionFactory = configuration.buildSessionFactory();

        final Session currentSession = sessionFactory.openSession();
        currentSession.beginTransaction();

        Role role1 = new Role();
        role1.setName("ROLE_USER");

        Role role2 = new Role();
        role2.setName("ROLE_ADMIN");

        User user1 = new User();
        user1.setUserId("testuser");
        user1.setName("testuser");
        user1.setPassword("testuser");
        user1.setActive(1);
        final HashSet<Role> roles1 = new HashSet<Role>();
        roles1.add(role1);
        user1.setRoles(roles1);
        role1.addUser(user1);

        User user2 = new User();
        user2.setUserId("artur");
        user2.setName("artur");
        user2.setPassword("123");
        user2.setActive(1);
        final HashSet<Role> roles2 = new HashSet<>();
        roles2.add(role1);
        roles2.add(role2);
        user2.setRoles(roles2);
        role1.addUser(user2);
        role2.addUser(user2);

        currentSession.save(user1);
        currentSession.save(user2);

        currentSession.getTransaction().commit();
        currentSession.flush();

        currentSession.close();
        sessionFactory.close();


    }
}